import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
user_input = input("Enter your prompt for the model: ")
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": user_input,
        }
    ],
    temperature=1,
    top_p=1,
    model=model
)

print(response.choices[0].message.content)