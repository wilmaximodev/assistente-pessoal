from gemini import genai
import gradio as gr

initial_prompt = (
    "Você é um assistente de receitas culinárias. Você fornece receitas baseadas nos ingredientes fornecidos"
    "dá dicas de culinária e responde a perguntas sobre preparação de pratos."
)

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initial_prompt)

chat = model.start_chat()

def gradio_wrapper(message, _history):
    response = chat.send_message(message)
    return response.text

chat_interface = gr.ChatInterface(gradio_wrapper, title="Assistente de Receitas Culinárias 🍳")
chat_interface.launch()
