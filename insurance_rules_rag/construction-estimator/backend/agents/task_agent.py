from graph.state import ConstructionState
from openai import OpenAI
from config import OPENROUTER_API_KEY
import json


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


def task_agent(state: ConstructionState):

    print("Task Agent Running")

    pdf_text = state["pdf_text"]

    prompt = f"""
You are a construction plan analysis expert.

Analyze the following construction information.

Return ONLY valid JSON.

Example:

{{
  "walls": 2,
  "kitchen": 1,
  "pipeline": 15
}}

Construction Data:

{pdf_text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result_text = response.choices[0].message.content.strip()
    print("AI RESPONSE:")
    print(result_text)
    try:
        state["detected_tasks"] = json.loads(result_text)
    except Exception:
        state["detected_tasks"] = {
            "walls": 0,
            "kitchen": 0,
            "pipeline": 0
        }

    return state