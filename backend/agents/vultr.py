import os
from openai import OpenAI

# Initialize the client using Vultr credentials
client = OpenAI(
    api_key=os.environ.get("VULTR_INFERENCE_API_KEY"),
    base_url="https://api.vultr.com/v1/inference" # Confirm exact endpoint in your portal
)

def query_enterprise_agent(prompt, model="llama3-8b-instruct"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an Enterprise Operations AI Agent."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
