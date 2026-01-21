import json
import os
import urllib.parse

# Configurações do seu GitHub
USER = "chengcheng-gm"
REPO = "launcherradio-init"
BASE_URL = f"https://raw.githubusercontent.com/{USER}/{REPO}/main/musicas/"

playlist = {"tracks": []}

# Lista todos os arquivos .mp3 da pasta
arquivos = [f for f in os.listdir('.') if f.lower().endswith('.mp3')]
arquivos.sort() # Deixa em ordem (01, 02, 03...)

for nome_arquivo in arquivos:
    # Transforma espaços e caracteres especiais para formato de URL (ex: %20)
    url_formatada = BASE_URL + urllib.parse.quote(nome_arquivo)
    
    # Remove o .mp3 do título para ficar limpo
    titulo = nome_arquivo.replace(".mp3", "")
    
    playlist["tracks"].append({
        "title": titulo,
        "url": url_formatada
    })

# Salva o arquivo playlist.json
with open('playlist.json', 'w', encoding='utf-8') as f:
    json.dump(playlist, f, indent=2, ensure_ascii=False)

print(f"Sucesso! {len(arquivos)} músicas foram adicionadas ao playlist.json")