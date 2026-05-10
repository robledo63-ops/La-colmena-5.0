import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

# 1. Definimos el modelo fuera para que sea global
llm = ChatGroq(
    model_name="llama3-70b-8192",
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

# 2. Definimos al Agente
consultor = Agent(
    role='Consultor de Automatización',
    goal='Optimizar procesos para Inmobiliaria Bajakey',
    backstory='Experto en n8n y Make en Tijuana.',
    llm=llm,
    verbose=True
)

# 3. Definicion de la Tarea
tarea = Task(
    description='Guía para conectar WhatsApp con n8n.',
    expected_output='Lista de 5 pasos técnicos.',
    agent=consultor
)

# 4. Creación de la Crew
colmena = Crew(
    agents=[consultor],
    tasks=[tarea],
    verbose=True
)

# ESTA PARTE ES LA MÁS IMPORTANTE PARA LA NUBE:
if __name__ == "__main__":
    colmena.kickoff()
