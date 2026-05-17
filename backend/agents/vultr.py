import os
from openai import OpenAI

# Initialize the client using Vultr credentials
client = OpenAI(
    api_key=os.environ.get("VULTR_INFERENCE_API_KEY"),
    base_url="https://api.vultrinference.com/v1" # Correct Vultr Serverless Inference endpoint
)

def query_enterprise_agent(prompt, model="llama-3.1-70b-instruct-fp8"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an Enterprise Operations AI Agent."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
