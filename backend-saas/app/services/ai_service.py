from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_task_suggestions(preferences: list[str]) -> list[str]:
    """
    Gera sugestões de tarefas com base nas preferências do usuário.
    """
    prompt = f"Gere uma lista de tarefas diárias para um usuário interessado em {', '.join(preferences)}."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    tasks = response.choices[0].message.content.split("\n")
    return [task.strip() for task in tasks if task.strip()]