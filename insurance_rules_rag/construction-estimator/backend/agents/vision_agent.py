import fitz
import base64

from openai import OpenAI
from config import OPENROUTER_API_KEY
from graph.state import ConstructionState

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


def vision_agent(state: ConstructionState):
    print("Vision Agent Running")

    pdf_path = state.get("pdf_path")

    if not pdf_path:
        return state

    doc = fitz.open(pdf_path)
    page = doc[0]

    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    image_bytes = pix.tobytes("png")

    doc.close()

    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """
Analyze this construction plan.

Identify:
- walls
- rooms
- kitchen
- bathrooms
- pipelines
- demolition work

Return a detailed analysis.
"""
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )

    vision_analysis = response.choices[0].message.content

    print("VISION ANALYSIS:")
    print(vision_analysis)

    state["pdf_text"] = vision_analysis

    return state