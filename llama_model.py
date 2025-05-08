import ollama

def ask_llama(context: str, question: str) -> str:
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    response = ollama.chat(model='llama3.2', messages=[
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]
