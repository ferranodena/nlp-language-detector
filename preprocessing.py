import os
import re
import json
import random

def preprocess_text(text):
    # 1. Eliminar dígits
    text = re.sub(r'\d', '', text)
    
    # 2. Convertir a minúscula
    text = text.lower()
    
    # 3. Substituir espais o tabulacions seguits per un de sol 
    text = re.sub(r'[ \t]+', ' ', text)
    
    # 4. Eliminar espais en blanc que hi pugui haver just abans o després d'un salt de línia
    text = re.sub(r' *\n *', '\n', text)
    
    # 5. ARA SÍ: Convertir tots els salts de línia a un doble espai i blindar-los
    text = re.sub(r'\n+', '  ', text)
    
    # 6. Eliminar espais inicials i finals de tot l'arxiu
    text = text.strip()
    
    return text

def process_and_split_train_folder(input_folder, preprocessed_folder, train_json_path, test_json_path, split_ratio=0.8):
    """
    Llegeix els arxius només de la carpeta train, els preprocessa i els divideix 
    en un 80% per a train i un 20% per a test, guardant-ho en dos JSON separats.
    """
    if not os.path.exists(preprocessed_folder):
        os.makedirs(preprocessed_folder)

    if not os.path.exists(input_folder):
        print(f"Error: La carpeta '{input_folder}' no existeix.")
        return

    languages = {'deu', 'eng', 'fra', 'ita', 'nld', 'spa'}
    corpus_train = {}
    corpus_test = {}

    print(f"\n=== Processant dades de '{input_folder}' per fer l'split 80/20 ===")

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            lang_code = filename.split('_')[0]
            
            if lang_code in languages:
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(preprocessed_folder, filename)

                # 1. Llegir l'arxiu
                with open(input_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 2. Preprocessar
                processed_full_text = preprocess_text(content)

                # Guardar el .txt complet preprocessat com a còpia de seguretat
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(processed_full_text)

                # 3. Fer l'Split 80/20 per FRASES
                # Separem el text pel doble espai que actua com a separador de salts de línia
                frases = re.split(r' {2,}', processed_full_text)
                
                # Eliminem elements buits residuals
                frases = [f for f in frases if f.strip()]

                # Barregem les frases abans de partir perquè sigui homogeni
                # random.seed(42) # Descomenta això si vols que l'split 80/20 sempre agafi les mateixes frases
                random.shuffle(frases)

                # Calculem quin és l'índex que marca el 80%
                split_index = int(len(frases) * split_ratio)

                # Repartim les frases
                train_frases = frases[:split_index]
                test_frases = frases[split_index:]

                # Les tornem a ajuntar amb un doble espai per mantenir el mateix format als JSON
                corpus_train[lang_code] = "  ".join(train_frases)
                corpus_test[lang_code]  = "  ".join(test_frases)

                print(f"Processat: {filename} → {len(train_frases)} frases a Train (80%), {len(test_frases)} a Test (20%)")

    # 4. Guardar els arxius JSON
    with open(train_json_path, 'w', encoding='utf-8') as f:
        json.dump(corpus_train, f, ensure_ascii=False, indent=2)

    with open(test_json_path, 'w', encoding='utf-8') as f:
        json.dump(corpus_test, f, ensure_ascii=False, indent=2)

    print(f"\nJSON generats:")
    print(f" - Train: {train_json_path}")
    print(f" - Test : {test_json_path}\n")

# ==========================================
# EXECUCIÓ
# ==========================================
input_folder        = './train'                   # NOMÉS toquem train
preprocessed_folder = './preprocessed_train'
train_json_path     = './corpus_train.json'
test_json_path      = './corpus_test.json'

process_and_split_train_folder(input_folder, preprocessed_folder, train_json_path, test_json_path, split_ratio=0.8)
