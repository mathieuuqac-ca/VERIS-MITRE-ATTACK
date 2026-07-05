# Semaine 7 — Contribution E3

## Consigne E3

Construire la base vectorielle à partir des descriptions de techniques ATT&CK et intégrer la récupération dans le pipeline d'inférence.

## Ce qui a été ajouté

Fichiers principaux :

```text
src/e3_pipeline/fetch_attack_stix.py
src/e3_pipeline/build_attack_vector_store.py
src/e3_pipeline/attack_rag_retriever.py
src/e3_pipeline/rag_inference_wrapper.py
prompts/rag_prompt.txt
configs/rag_config.json
requirements_week7.txt
scripts/run_week7_rag.ps1
```

## Pourquoi cette étape est utile

En zéro-shot ou few-shot, le LLM peut inventer des techniques ATT&CK ou oublier des techniques pertinentes.

L'approche RAG ajoute une étape de récupération avant le prompt :
1. on encode les descriptions ATT&CK dans une base vectorielle ;
2. pour chaque incident VCDB/VERIS, on récupère les techniques ATT&CK les plus proches ;
3. on donne ces candidats au LLM ;
4. le LLM choisit parmi des techniques plus pertinentes et mieux contextualisées.

Cette étape rend l'inférence plus guidée, plus explicable et plus reproductible.

## Pipeline mis en place

```text
MITRE ATT&CK STIX JSON
        ↓
Extraction des techniques ATT&CK
        ↓
Construction du texte RAG par technique
        ↓
Vectorisation TF-IDF
        ↓
Base vectorielle locale
        ↓
Incident VCDB normalisé
        ↓
Récupération top-k techniques ATT&CK
        ↓
Prompt RAG
        ↓
Prédiction JSON structurée
```

## Backend utilisé

Le script supporte :
- backend `sklearn`, par défaut, robuste sous Windows ;
- backend `faiss`, optionnel si `faiss-cpu` est installé.

Même si le backend par défaut utilise scikit-learn plutôt que FAISS, la logique correspond bien à une base vectorielle RAG : les descriptions ATT&CK sont encodées dans un espace vectoriel et les candidats sont récupérés par similarité.

## Commandes

Installer les dépendances :

```powershell
python -m pip install -r requirements_week7.txt
```

Définir le chemin source :

```powershell
$env:PYTHONPATH = "$PWD\src"
```

Télécharger ATT&CK STIX :

```powershell
python -m e3_pipeline.fetch_attack_stix
```

Construire la base vectorielle :

```powershell
python -m e3_pipeline.build_attack_vector_store --backend sklearn
```

Tester une requête libre :

```powershell
python -m e3_pipeline.attack_rag_retriever --query "phishing email credential theft" --top-k 5
```

Récupérer des candidats pour les incidents VCDB :

```powershell
python -m e3_pipeline.attack_rag_retriever --input data/processed/incidents_clean.jsonl --top-k 5 --limit 5
```

Lancer l'inférence RAG en mode mock :

```powershell
python -m e3_pipeline.rag_inference_wrapper --mock --top-k 5 --limit 5
```

## Sorties générées

```text
data/raw/attack/enterprise-attack.json
data/processed/attack/attack_techniques.jsonl
data/processed/attack/attack_techniques.csv
outputs/rag/attack_vector_store/
outputs/rag/rag_candidates.jsonl
outputs/rag/rag_candidates_summary.csv
outputs/rag/rag_predictions_mock.jsonl
```

## Ce que je peux dire au professeur

Pour la semaine 7, j'ai construit la base vectorielle ATT&CK et intégré la récupération dans le pipeline d'inférence.

J'ai ajouté un script qui récupère le fichier Enterprise ATT&CK au format STIX/JSON, extrait les techniques ATT&CK, leurs descriptions, tactiques, plateformes et sources de données, puis construit un texte de recherche pour chaque technique.

Ensuite, j'ai vectorisé ces descriptions avec TF-IDF et construit une base de similarité. Pour chaque incident VCDB normalisé, le pipeline récupère les top-k techniques ATT&CK les plus proches. Ces candidats sont ensuite injectés dans un prompt RAG pour guider l'inférence.

J'ai validé la chaîne en mode mock afin de tester l'intégration sans consommer d'appels API. Cela produit des candidats ATT&CK et des prédictions structurées en JSON.
