import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

def run():
    # Configuramos el modelo con la variable de la plataforma
    llm = ChatGroq(
        model_name="llama3-70b-8192",
        groq_api_key=os.environ.get("GROQ_API_KEY")
    )

    consultor = Agent(
        role='Consultor de Automatización',
        goal='Optimizar procesos para Inmobiliaria Bajakey',
        backstory='Experto en n8n y Make en Tijuana.',
        llm=llm,
        verbose=True
    )

    tarea = Task(
        description='Guía técnica para conectar WhatsApp con n8n.',
        expected_output='Lista de 5 pasos claros.',
        agent=consultor
    )

    colmena = Crew(
        agents=[consultor],
        tasks=[tarea],
        verbose=True
    )

    return colmena.kickoff()

if __name__ == "__main__":
    run()
