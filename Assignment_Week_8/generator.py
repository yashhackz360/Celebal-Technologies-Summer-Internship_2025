# Option 1: OpenAI GPT-3.5
import openai

def generate_with_openai(contexts, query, api_key):
    openai.api_key = api_key
    context = "\n".join(contexts)
    prompt = f"""Answer the following question based on the given context:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']


# Option 2: Hugging Face (Mistral 7B)
from transformers import pipeline

hf_pipeline = pipeline("text-generation", model="tiiuae/falcon-rw-1b", max_new_tokens=200) 

def generate_with_huggingface(contexts, query):
    context = "\n".join(contexts)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    result = hf_pipeline(prompt)[0]["generated_text"]
    return result.split("Answer:")[-1].strip()
