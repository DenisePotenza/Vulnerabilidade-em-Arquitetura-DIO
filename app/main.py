import os
from openai import AzureOpenAI

# Pega configs do .env
endpoint = os.getenv("OAI_ENDPOINT")
key = os.getenv("OAI_KEY")
deployment = os.getenv("OAI_DEPLOYMENT")
api_version = os.getenv("OAI_API_VERSION", "2023-12-01-preview")

# Cria cliente
client = AzureOpenAI(
    api_key=key,
    azure_endpoint=endpoint,
    api_version=api_version
)

def analyze_architecture(prompt: str):
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a security expert doing STRIDE analysis."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content