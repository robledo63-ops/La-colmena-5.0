import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

# Configuración del modelo
llm = ChatGroq(
    model_name="llama3-70b-8192",
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

# Definición del Agente
consultor = Agent(
    role='Consultor de Automatización',
    goal='Optimizar procesos para Inmobiliaria Bajakey',
    backstory='Experto en n8n y Make en Tijuana.',
    llm=llm,
    verbose=True
)

# Definición de la Tarea
tarea = Task(
    description='Guía técnica para conectar WhatsApp con n8n.',
    agent=consultor,
    expected_output='Lista de 5 pasos técnicos claros.'
)

# Ejecución directa
colmena = Crew(
    agents=[consultor],
    tasks=[tarea],
    verbose=True
)

# Esto hace que corra en cuanto la plataforma lo abra
if __name__ == "__main__":
    colmena.kickoff()
