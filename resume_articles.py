#resume_articles.py
import google.generativeai as genai
import os
import PyPDF2

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

# vou ler um pdf e fazer um resumo conciso de um artigo cientifico

with open("artigoPDF/artigo_cientifico_IA.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    texto = ""
    for page in reader.pages:
        texto += page.extract_text()
        
prompt = f"Por favor, resuma o seguinte artigo cientifico de forma concisa:\n{texto}"

response = model.generate_content(prompt)

print("Resumo do Artigo Científico:")
print(response.text)