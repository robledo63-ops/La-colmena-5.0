import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

def run():
    # 1. Configuración del modelo (Lee la llave que pusiste en la plataforma)
    llm_model = ChatGroq(
        model_name="llama3-70b-8192",
        groq_api_key=os.environ.get("GROQ_API_KEY")
    )

    # 2. Definición del Agente
    consultor = Agent(
        role='Consultor de Automatización',
        goal='Analizar procesos para Inmobiliaria Bajakey',
        backstory='Experto en n8n y Make en Tijuana.',
        llm=llm_model,  # <-- Esto arregla el ValidationError
        verbose=True
    )

    # 3. Definición de la Tarea
    tarea = Task(
        description='Pasos técnicos para conectar WhatsApp con n8n.',
        expected_output='Guía de 5 pasos claros.',
        agent=consultor
    )

    # 4. Creación de la Crew
    colmena = Crew(
        agents=[consultor],
        tasks=[tarea],
        verbose=True
    )

    return colmena.kickoff()

if __name__ == "__main__":
    run()
