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
    with open("test_plan.png", "wb") as f:
        f.write(image_bytes)

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
You are a professional construction estimator and architectural plan analyst.

Analyze the attached construction plan image.

Your task is to identify and estimate:

- Number of walls
- Number of rooms
- Number of kitchens
- Number of bathrooms
- Number of doors
- Number of windows
- Length of plumbing pipelines
- Demolition areas
- Renovation work
- Structural elements

If information is unclear, provide your best estimate based on the visual plan.

Do NOT say that you cannot analyze the image.
Do NOT refuse the task.

Return a detailed construction analysis including quantities and observations.
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
        ],
        temperature=0
    )

    vision_analysis = response.choices[0].message.content

    print("VISION ANALYSIS:")
    print(vision_analysis)

    state["pdf_text"] = vision_analysis

    return state