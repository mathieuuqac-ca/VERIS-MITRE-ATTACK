# Semaine 5 — Contribution E3

## Consigne E3

Automatiser la récupération d'exemples par similarité depuis l'ensemble d'entraînement et journaliser toutes les expériences avec MLflow ou Weights & Biases.

## Ce qui a été ajouté

Pour répondre à cette consigne, j'ai ajouté une brique de récupération d'exemples similaires.

Le principe est le suivant :

1. lire les incidents normalisés produits en semaine 2 ;
2. transformer chaque incident en texte de comparaison ;
3. vectoriser les incidents avec TF-IDF ;
4. calculer la similarité cosinus entre les incidents ;
5. récupérer les top-k incidents les plus proches pour chaque requête ;
6. produire un fichier JSONL exploitable par les prompts few-shot ;
7. journaliser les paramètres, métriques et artefacts de l'expérience.

## Pourquoi cette étape est utile

En semaine 5, E1 travaille sur les prompts few-shot. Pour faire du few-shot, il faut fournir au modèle quelques exemples pertinents.

Le problème est que choisir les exemples manuellement est long, subjectif et peu reproductible.

Mon travail E3 permet d'automatiser cette sélection : pour chaque incident cible, le script retrouve automatiquement les incidents les plus similaires dans l'ensemble d'entraînement.

Cela rend les prompts few-shot plus cohérents et plus reproductibles.

## Fichiers ajoutés

```text
src/e3_pipeline/example_retriever.py
src/e3_pipeline/build_few_shot_requests.py
src/e3_pipeline/experiment_tracker.py
prompts/few_shot_prompt.txt
scripts/run_week5_similarity.ps1
requirements_week5.txt
```

## Commandes utilisées

Installer les dépendances de la semaine 5 :

```powershell
pip install -r requirements_week5.txt
```

Lancer la récupération d'exemples similaires :

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m e3_pipeline.example_retriever --top-k 3 --limit 20
```

Construire les requêtes few-shot :

```powershell
python -m e3_pipeline.build_few_shot_requests --limit 5
```

## Sorties générées

```text
outputs/retrieved_examples.jsonl
outputs/retrieved_examples_summary.csv
outputs/few_shot_requests.jsonl
outputs/experiments/
logs/example_retriever.log
```

## Journalisation

La journalisation locale est toujours active. À chaque exécution, un dossier est créé dans :

```text
outputs/experiments/
```

Il contient :

```text
params.json
metrics.json
summary.json
retrieved_examples.jsonl
retrieved_examples_summary.csv
```

Si MLflow est installé et que l'option --mlflow est utilisée, les paramètres et métriques sont aussi envoyés dans MLflow.

Commande avec MLflow :

```powershell
python -m e3_pipeline.example_retriever --top-k 3 --limit 20 --mlflow
```

## Ce que je peux dire au professeur

Pour la semaine 5, j'ai ajouté une étape d'automatisation de la sélection d'exemples few-shot. Le script utilise les incidents normalisés de la semaine 2, construit une représentation textuelle de chaque incident avec le narratif et les champs VERIS, puis récupère les incidents les plus similaires avec TF-IDF et similarité cosinus.

Les exemples récupérés sont exportés en JSONL et CSV. J'ai aussi généré un fichier de requêtes few-shot prêt à être utilisé par E1 dans ses prompts. Enfin, chaque expérience est journalisée avec ses paramètres, ses métriques et ses artefacts dans outputs/experiments/, avec une option MLflow si nécessaire.
