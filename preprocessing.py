import os
import re

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

def process_corpus_files(input_folder, preprocessed_langId):
    if not os.path.exists(preprocessed_langId):
        os.makedirs(preprocessed_langId)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(preprocessed_langId, filename)
            
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            processed = preprocess_text(content)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(processed)
            
            print(f"Processed: {filename}")

# Ús
input_folder = './langId'
preprocessed_langId = './preprocessed_landId'
process_corpus_files(input_folder, preprocessed_langId)