from openai import AzureOpenAI

CLIENT = AzureOpenAI(
    api_key="FUwFEsKnzCNeaB4l3xW3HpybYreDgrMkcp35LfSRBeYA0idPxOr7JQQJ99AJACHYHv6XJ3w3AAABACOG0FFq",
    api_version="2024-02-01",
    azure_endpoint="https://jg003-m2vyznzu-eastus2.openai.azure.com/openai/deployments/whisper/audio/translations?api-version=2024-06-01"
)