from openai import OpenAI
from config import OPENROUTER_API_KEY

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
"text": "Describe this image"
},
{
"type": "image_url",
"image_url": {
"url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg"
}
}
]
}
]
)

print(response.choices[0].message.content)
