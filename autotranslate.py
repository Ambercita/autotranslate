# Configuración inicial

INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'
HOST_URL = 'http://localhost:5000'

# zh - Chinese, en - English, es - Spanish

INPUT_LANG = 'zh'
OUTPUT_LANG = 'es'

import os
import requests

def translate_file(file, target_lang, source_lang):
    url = f'{HOST_URL}/translate_file'
    input_file = open(file, 'rb')
    files = {'file': input_file}
    data = {'target': target_lang, 'source': source_lang}
    response = requests.post(url, files=files, data=data)
    input_file.close()
    return response.json()

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
        file.close()

for file in os.listdir(INPUT_FOLDER):
    file = os.path.join(INPUT_FOLDER, file)
    response = translate_file(file, OUTPUT_LANG, INPUT_LANG)
    output_path = os.path.join(OUTPUT_FOLDER, os.path.basename(file))
    if 'translatedFileUrl' in response:
        download_file(response['translatedFileUrl'], output_path)
        print(f'Translated {file} to {output_path}')
    else:
        print(f'Error translating {file}')