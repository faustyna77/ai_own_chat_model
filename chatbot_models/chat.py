import os
import openai
from dotenv import load_dotenv
import time

# Ładowanie zmiennych środowiskowych z pliku .env
load_dotenv()

# Konfiguracja klienta Azure OpenAI
openai.api_type = "azure"
openai.api_base = "https://zasob.openai.azure.com/"
openai.api_version = "2023-09-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai():
    print("Rozmowa z AI - aby zakończyć, wpisz 'koniec'")
    
    conversation = []
    while True:
        user_input = input("Ty: ")
        if user_input.lower() == 'koniec':
            print("Zakończono rozmowę.")
            break

        # Dodajemy wypowiedź użytkownika do historii rozmowy
        conversation.append(f"Human: {user_input}")
        
        # Tworzymy ciągły prompt na podstawie historii rozmowy
        prompt = "\n".join(conversation) + "\nAI:"
        time.sleep(6)
        
        # Wysłanie promptu do modelu AI
        response = openai.Completion.create(
            engine="zasob",  # zmień na nazwę swojego deploymentu
            prompt=prompt,
            temperature=0.9,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["Human:", "AI:"]
        )
        
        # Pobieranie odpowiedzi z modelu AI
        ai_response = response['choices'][0]['text'].strip()
        
        # Drukowanie odpowiedzi AI
        print(f"AI: {ai_response}")
        
        # Dodawanie odpowiedzi AI do historii rozmowy
        conversation.append(f"AI: {ai_response}")

if __name__ == "__main__":
    chat_with_ai()
