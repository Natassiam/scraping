import requests
from bs4 import BeautifulSoup
import base64
import re

# URL da página
url = "https://www.example.com"  # Substitua pela URL real"

# Faz a requisição da página
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Busca a tag <img>
img_tag = soup.find("img")

if img_tag and "src" in img_tag.attrs:
    src = img_tag["src"]

    if src.startswith("data:image"):
        # Extrai o tipo da imagem e os dados base64
        match = re.match(r'data:image/(.+);base64,(.*)', src)
        if match:
            image_type = match.group(1)
            base64_data = match.group(2)

            # Decodifica os dados base64
            image_data = base64.b64decode(base64_data)

            # Salva a imagem com extensão correta
            filename = f"imagem_extraida.{image_type}"
            with open(filename, "wb") as f:
                f.write(image_data)
            print(f"Imagem salva como {filename}")
        else:
            print("Formato de imagem base64 inválido.")
    else:
        print("Imagem não está embutida como base64.")
else:
    print("Tag <img> não encontrada ou sem atributo 'src'.")
