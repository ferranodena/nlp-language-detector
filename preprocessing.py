import os
import re
import json


def preprocess_text(text):
    # 1. Eliminar dígits
    text = re.sub(r'\d', '', text)
    
    # 2. Convertir a minúscula
    text = text.lower()
    
    # 3. Substituir salts de línia per un doble espai
    text = re.sub(r'\n+', '  ', text)
    
    # 4. Substituir altres espais en blanc continus per un sol espai
    text = re.sub(r'[ \t]+', ' ', text)
    
    # 5. Eliminar espais inicials i finals
    text = text.strip()
    
    return text


def process_corpus_files(input_folder, preprocessed_folder):
    if not os.path.exists(preprocessed_folder):
        os.makedirs(preprocessed_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(preprocessed_folder, filename)

            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            processed = preprocess_text(content)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(processed)

            print(f"Processed: {filename}")


def merge_txt_to_json(preprocessed_folder, output_json_path):
    corpus = {}
    languages = {'deu', 'eng', 'fra', 'ita', 'nld', 'spa'}

    for filename in os.listdir(preprocessed_folder):
        if filename.endswith('.txt'):
            lang_code = filename.split('_')[0]  # Exemple: 'eng' a partir de 'eng_trn.txt'
            if lang_code in languages:
                filepath = os.path.join(preprocessed_folder, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    corpus[lang_code] = f.read()
                print(f"Added to JSON: {filename} → '{lang_code}'")

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(corpus, f, ensure_ascii=False, indent=2)

    print(f"JSON guardat a: {output_json_path} ({len(corpus)} idiomes)\n")


def process_split(folder_name):
    """Processa una carpeta directament (ex: 'train' o 'test')."""
    input_folder        = f'./{folder_name}'
    preprocessed_folder = f'./preprocessed_{folder_name}'
    output_json         = f'./corpus_{folder_name}.json'

    print(f"\n=== Processant la carpeta '{input_folder}' ===")
    
    # Comprovem que la carpeta d'entrada existeixi per evitar errors
    if not os.path.exists(input_folder):
        print(f"Atenció: La carpeta '{input_folder}' no existeix. Es saltarà.")
        return

    process_corpus_files(input_folder, preprocessed_folder)
    merge_txt_to_json(preprocessed_folder, output_json)


# Executem el procés per a les carpetes 'train' i 'test'
carpetes_a_processar = ['train', 'test']

for carpeta in carpetes_a_processar:
    process_split(carpeta)
