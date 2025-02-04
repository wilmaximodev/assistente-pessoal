from gemini import genai

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

with open("translated/documento_portugues.txt", "r", encoding="utf-8") as file:
    texto_portugues = file.read()

prompt = f"Por favor, traduza o seguinte texto para o inglês:\n{texto_portugues}"

response = model.generate_content(prompt)

with open("translated/documento_ingles.txt", "w", encoding="utf-8") as file:
    file.write(response.text)
print("Tradução concluída e salva em 'documento_ingles.txt'.")

