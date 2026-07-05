# Semaine 6 — Contribution E3

## Consigne E3

Configurer l'environnement d'entraînement, gérer les checkpoints, surveiller la mémoire GPU et la courbe de loss.

## Ce qui a été ajouté

Pour répondre à cette consigne, j'ai ajouté une infrastructure de suivi d'entraînement.

Fichiers principaux :

```text
src/e3_pipeline/gpu_check.py
src/e3_pipeline/mock_training_run.py
src/e3_pipeline/training_monitor.py
src/e3_pipeline/checkpoint_manager.py
configs/training_config.json
requirements_week6.txt
scripts/run_week6_mock.ps1
```

## Pourquoi faire cela ?

Même si E1 est responsable du fine-tuning du modèle, mon rôle E3 est de préparer l'environnement technique.

Le fine-tuning peut être coûteux et instable : manque de mémoire GPU, checkpoints trop nombreux, courbe de loss non suivie, environnement difficile à reproduire.

L'objectif est donc de sécuriser l'entraînement avant de lancer un vrai modèle.

## Étapes techniques

### 1. Vérification de l'environnement

Le script `gpu_check.py` vérifie :
- version de Python ;
- système d'exploitation ;
- présence de PyTorch ;
- disponibilité CUDA ;
- nombre de GPU ;
- mémoire GPU si disponible ;
- sortie de `nvidia-smi` si disponible.

Sortie générée :

```text
outputs/training_environment_report.json
```

### 2. Simulation d'entraînement

Le script `mock_training_run.py` simule un entraînement pour tester l'infrastructure sans GPU.

Il génère :
- une courbe de loss simulée ;
- des checkpoints ;
- un fichier `trainer_state.json` ;
- un log simulé de mémoire GPU.

Cette étape permet de tester la gestion des checkpoints et la génération des courbes sans attendre le vrai fine-tuning de E1.

### 3. Monitoring de l'entraînement

Le script `training_monitor.py` lit le fichier `trainer_state.json` et produit :
- `loss_history.csv` ;
- `loss_curve.png` ;
- `checkpoints_summary.csv` ;
- `training_monitor_report.json`.

Cela permet de suivre l'évolution de la loss et de vérifier si l'entraînement semble converger.

### 4. Gestion des checkpoints

Le script `checkpoint_manager.py` liste les checkpoints et peut supprimer les anciens pour garder seulement les derniers.

Exemple :

```powershell
python -m e3_pipeline.checkpoint_manager --run-dir outputs/training_runs/mock_week6_run --keep-last 2
```

Cela évite de saturer le stockage pendant un entraînement long.

## Commandes lancées

Installation des dépendances :

```powershell
python -m pip install -r requirements_week6.txt
```

Activation du chemin source :

```powershell
$env:PYTHONPATH = "$PWD\src"
```

Vérification environnement :

```powershell
python -m e3_pipeline.gpu_check
```

Simulation d'entraînement :

```powershell
python -m e3_pipeline.mock_training_run --steps 60 --checkpoint-every 20
```

Monitoring :

```powershell
python -m e3_pipeline.training_monitor --run-dir outputs/training_runs/mock_week6_run
```

Gestion des checkpoints :

```powershell
python -m e3_pipeline.checkpoint_manager --run-dir outputs/training_runs/mock_week6_run --keep-last 2
```

## Sorties attendues

```text
outputs/training_environment_report.json
outputs/training_runs/mock_week6_run/trainer_state.json
outputs/training_runs/mock_week6_run/loss_history.csv
outputs/training_runs/mock_week6_run/loss_curve.png
outputs/training_runs/mock_week6_run/checkpoints_summary.csv
outputs/training_runs/mock_week6_run/training_monitor_report.json
outputs/training_runs/mock_week6_run/checkpoint_manager_report.json
```

## Ce que je peux dire au professeur

Pour la semaine 6, j'ai préparé l'infrastructure d'entraînement. J'ai ajouté un script pour vérifier l'environnement GPU et PyTorch, un fichier de configuration d'entraînement, un système de suivi des checkpoints et un script de monitoring de la loss.

Comme le vrai fine-tuning dépend du modèle choisi par E1 et de l'accès à un GPU, j'ai aussi créé un entraînement simulé. Cela permet de tester la chaîne technique sans GPU : création de checkpoints, extraction de la courbe de loss, génération d'un graphique et nettoyage des anciens checkpoints.

Cette infrastructure pourra ensuite être branchée sur le vrai entraînement de E1, par exemple sur Colab Pro ou un environnement HPC.
