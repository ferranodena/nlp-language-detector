# NLP Language Detector

This repository contains the implementation of a statistical generative language model designed to automatically detect the language of a given text. The project is based on character trigrams and explores two different smoothing techniques to handle zero-probability issues for unseen n-grams.

The model is trained and evaluated using the **Leipzig Corpora Collection**, supporting 6 different languages: German (`deu`), English (`eng`), French (`fra`), Italian (`ita`), Dutch (`nld`), and Spanish (`spa`).

## 🚀 Features

- **Data Preprocessing**: Cleans texts, standardizes formats, and concatenates sentences using double spaces to ensure proper trigram extraction at word and sentence boundaries.
- **Trigram-based Generative Model**: Uses Maximum Likelihood Estimation (MLE) combined with logarithmic probabilities to efficiently classify text.
- **Lidstone Smoothing**: Adds a $\lambda$ parameter to handle out-of-vocabulary trigrams. Includes a custom K-Fold Cross-Validation method to find the optimal $\lambda$ for each language.
- **Interpolation Smoothing**: Combines probabilities from trigrams, bigrams, unigrams, and a uniform distribution using specific weights ($\lambda_3, \lambda_2, \lambda_1, \lambda_0$) for more robust predictions.

## 📊 Models & Results

The evaluation was performed on a test set containing 6,000 sentences per language (36,000 sentences in total). Both models achieved near-perfect performance.

### 1. Lidstone Smoothing Model

After optimizing the $\lambda$ parameter through cross-validation, the model achieved an exceptional overall accuracy.

**Accuracy by Language:**

- German (`deu`): 99.73%
- English (`eng`): 99.97%
- French (`fra`): 99.97%
- Italian (`ita`): 99.72%
- Dutch (`nld`): 99.65%
- Spanish (`spa`): 99.70%

This is the confusion matrix for the Lidstone Smoothing Model:

![Confusion Matrix](./images/confusion_matrix_lidstone.png)

*Most errors in this model were due to short sentences containing foreign proper nouns (e.g., English names in German texts) or highly international terminology.*

### 2. Interpolation Smoothing Model

This model uses partial information (unigrams and bigrams) when exact trigrams are missing. The default weights used were: `0.05` (Uniform), `0.10` (Unigram), `0.25` (Bigram), and `0.60` (Trigram).

**Accuracy by Language:**

- German (`deu`): 99.60%
- English (`eng`): 99.68%
- French (`fra`): 99.97%
- Italian (`ita`): 99.77%
- Dutch (`nld`): 99.78%
- Spanish (`spa`): 99.90%

This is the confusion matrix for the Interpolation Smoothing Model:

![Confusion Matrix](./images/confusion_matrix_interpolation.png)

*Both models yielded an F1-Score of 1.00 across all classes, proving that character-based n-grams are highly effective for language identification.*

## 🛠️ Usage

### Prerequisites

Make sure you have the following libraries installed:

```bash
pip install nltk scikit-learn matplotlib seaborn numpy
```

## Repository Structure

Aquí tens l'estructura del repositori amb l'arbre de directoris indentat i descrit individualment per a cada element, basat exactament en la teva imatge:

## 📂 Project Structure

- `preprocessed_train/`: Directory containing the training text files after applying cleaning and formatting rules.
- `test/`: Directory with the raw text files reserved exclusively for evaluating the models.
- `train/`: Directory containing the original raw text data used to build the language models.
- `corpus_test.json`: Parsed and structured test dataset, grouped by language and divided into sentences.
- `corpus_train.json`: Parsed and structured training dataset, ready for feature extraction.
- `interpolation_model.json`: Saved parameters and probabilities for the fully trained Interpolation Smoothing model.
- `lidstone_model.json`: Saved parameters, trigram counts, and optimized lambdas for the Lidstone Smoothing model.
- `main.ipynb`: Core Jupyter Notebook containing the full pipeline, including training, cross-validation, and performance benchmarks.
- `preprocessing.py`: Core Python script responsible for data cleaning and text normalization.
- `trigrams_train.json`: Generated file containing the extracted character trigrams and their absolute frequencies per language.

## References

- Leipzig Corpora Collection: [https://corpora.uni-leipzig.de/en](https://corpora.uni-leipzig.de/en)
- Processament de Llenguatge Humà (NLP) course at UPC: [https://www.cs.upc.edu/~turmo/plh/plan15m/PLH.html](https://www.cs.upc.edu/~turmo/plh/plan15m/PLH.html)
---

This project is done as part of the Natural Language Processing course at the IA degree art Universitat Politècnica de Catalunya (UPC) during the 2025-2025 academic year.