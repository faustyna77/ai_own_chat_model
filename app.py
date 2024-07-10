import os
import requests

# Ustawienia API OpenAI
api_key = os.getenv("OPENAI_API_KEY")
endpoint = "https://faustyna.openai.azure.com/"

def generate_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(f"{endpoint}/chat/completions", json=data, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return None
    
    try:
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]
    except KeyError as e:
        print(f"Error: KeyError - {e}")
        return None

def main():
    while True:
        prompt = input("\nWyjaśnij definicję z fizyki lub zadaj pytanie: ")
        if prompt.lower() in ['quit', 'exit', 'q']:
            break
        
        response = generate_response(prompt)
        
        if response:
            print(f"Odpowiedź: {response}")
        else:
            print("Wystąpił błąd podczas przetwarzania zapytania.")

if __name__ == "__main__":
    main()
