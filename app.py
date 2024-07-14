import os
import openai

# Ustawienia dla API Azure OpenAI
openai.api_type = "azure"
openai.api_base = "https://zasob.openai.azure.com/"
openai.api_version = "2023-09-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

print("napisz co chesz wygenerować->")
answer=input()
# Wywołanie API dla uzyskania odpowiedzi
response = openai.Completion.create(
    engine="zasob",
    prompt=answer,
    temperature=1,
    max_tokens=100,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

# Wyświetlenie odpowiedzi
print(response["choices"][0]["text"])
