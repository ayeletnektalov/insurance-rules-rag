import fitz
import base64

from openai import OpenAI
from config import OPENROUTER_API_KEY

PDF_PATH = "uploads/הריסה.pdf"

# Convert first page of PDF to image

doc = fitz.open(PDF_PATH)
page = doc[0]

pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
image_bytes = pix.tobytes("png")

doc.close()

image_base64 = base64.b64encode(image_bytes).decode("utf-8")

client = OpenAI(
base_url="https://openrouter.ai/api/v1",
api_key=OPENROUTER_API_KEY
)

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

* walls
* rooms
* kitchen
* bathrooms
* pipelines
* demolition work

Describe everything you can identify.
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

print("\nVISION ANALYSIS:\n")
print(response.choices[0].message.content)
