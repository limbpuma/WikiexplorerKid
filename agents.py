# agents.py
import os
from dotenv import load_dotenv
import openai
from langchain.llms import OpenAI
from langchain.agents import Tool, initialize_agent
from helpers import load_content_from_wikipedia

# Cargar las variables de entorno
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Definir la herramienta de simplificación de texto
def text_simplifier_func(input_text: str) -> str:
    llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo")
    simplified_text = llm.predict(input_text)
    return simplified_text

# Registrar la herramienta de simplificación de texto
text_simplifier = Tool(
    name="text_simplifier",
    func=text_simplifier_func,
    description="Una herramienta para simplificar texto"
)

def initialize_kid_friendly_agent():
    # Cargar la herramienta de simplificación de texto
    tools = [text_simplifier]

    agent = initialize_agent(
        agent="zero-shot-react-description",
        tools=tools,
        llm=text_simplifier_func,  # Usar la función en lugar del modelo
        verbose=True,
        max_iterations=3
    )
    return agent

def adapt_content_for_kids(query):
    docs = load_content_from_wikipedia(query=query)
    agent = initialize_kid_friendly_agent()
    
    docs_text = '\n\n'.join([doc.page_content for doc in docs])
    
    prompt = (
        f"Como escritor especializado en educación infantil y usando un Simplificador de Texto, "
        f"tu tarea es adaptar y simplificar el siguiente contenido para hacerlo atractivo y fácil de "
        f"comprender para los niños. Asegúrate de que el lenguaje sea simple, claro y entretenido. "
        f"Incluye explicaciones y ejemplos donde sea necesario para explicar conceptos difíciles. "
        f"El objetivo es que un niño pueda leer y entender el contenido sin dificultad.\n\n{docs_text}"
    )
    result = agent(prompt)
    return result['output']
