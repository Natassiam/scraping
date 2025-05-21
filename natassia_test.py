import requests
from bs4 import BeautifulSoup
import base64
import re

# === CONFIGURAÇÕES ===
TOKEN = "" 
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
SCRAPE_URL = ""
INFERENCIA_URL = ""
SUBMIT_URL = ""

# === 1. FAZ SCRAPING DA IMAGEM BASE64 ===
response = requests.get(SCRAPE_URL)
soup = BeautifulSoup(response.text, "html.parser")
img_tag = soup.find("img")

if not img_tag or "src" not in img_tag.attrs or not img_tag["src"].startswith("data:image"):
    raise Exception("Imagem base64 não encontrada.")

match = re.match(r"data:image/(.+);base64,(.*)", img_tag["src"])
if not match:
    raise Exception("Formato de imagem base64 inválido.")

image_type = match.group(1)
base64_data = match.group(2)

# === 2. ENVIA A IMAGEM PARA INFERÊNCIA COMO JSON ===
json_payload = {
    "model": "microsoft-florence-2-large",
    "messages": [
        {
            "role": "user",
            "content": "<DETAILED_CAPTION>"
        }
    ],
    "image": {
        "format": image_type,
        "data": base64_data
    }
}

print("Enviando para inferência...")

inference_response = requests.post(
    INFERENCIA_URL,
    headers=HEADERS,
    json=json_payload
)

if inference_response.status_code != 200:
    print(" Erro na inferência:")
    print(inference_response.status_code)
    print(inference_response.text)
    exit()

json_response = inference_response.json()
print(" Inferência realizada com sucesso.")

# === 3. SUBMITE A RESPOSTA PARA AVALIAÇÃO ===
print("Enviando resposta para submissão...")

submit_response = requests.post(
    SUBMIT_URL,
    headers=HEADERS,
    json=json_response
)

if submit_response.status_code == 200:
    print("Resposta submetida com sucesso.")
else:
    print("Erro ao submeter a resposta:")
    print(submit_response.status_code)
    print(submit_response.text)
