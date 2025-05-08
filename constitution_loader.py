import requests
from bs4 import BeautifulSoup
import os

DATA_PATH = "data/constitution.txt"

def download_constitution(save_path=DATA_PATH):
    url = "https://www.akorda.kz/en/constitution-of-the-republic-of-kazakhstan-50912"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    content_div = soup.find("div", class_="content-text")
    if content_div:
        text = content_div.get_text(separator="\n", strip=True)
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(text)
    return save_path

def load_constitution_chunks(chunk_size=500):
    if not os.path.exists(DATA_PATH):
        download_constitution()

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        full_text = f.read()

    # Split into overlapping chunks
    chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]
    return chunks
