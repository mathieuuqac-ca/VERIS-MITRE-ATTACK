# Pipeline final — attendu du professeur et contribution E3

Le document du professeur demande un pipeline d'automatisation des expérimentations, une comparaison entre les techniques prédites par le modèle et les techniques assignées par l'expert, puis le calcul de VP, FP, FN, précision, rappel et F1.

## Ce module ajoute

- création d'un template de vérité terrain ;
- conversion de la vérité terrain en JSONL ;
- évaluation automatique des prédictions ;
- résultats par cas et par technique ;
- tableau comparatif entre expériences.

## Pipeline final

```text
VCDB / VERIS
    ↓
incidents_clean.jsonl
    ↓
LLM zéro-shot / RAG / modèle Hugging Face
    ↓
predictions JSONL
    ↓
truth expert : ground_truth_attack_mapping.jsonl
    ↓
VP / FP / FN
    ↓
precision / recall / F1
    ↓
experiments_comparison.csv
```

## Commandes

Créer le template à remplir :

```powershell
python -m e3_pipeline.create_ground_truth_template --limit 20
```

Remplir `data/processed/ground_truth_attack_mapping_template.csv`, colonne `expert_attack_ids`.

Convertir en JSONL :

```powershell
python -m e3_pipeline.build_ground_truth --incident-template data/processed/ground_truth_attack_mapping_template.csv
```

Évaluer :

```powershell
python -m e3_pipeline.evaluate_predictions --predictions outputs/predictions_zero_shot.jsonl --ground-truth data/processed/ground_truth_attack_mapping.jsonl --experiment-name zero_shot_mock
```

Comparer :

```powershell
python -m e3_pipeline.compare_experiments
```

## Phrase à dire au professeur

J'ai relié le pipeline E3 aux exigences finales : le système ne s'arrête plus aux prédictions. Il compare les techniques ATT&CK prédites avec la vérité terrain experte, calcule automatiquement les VP, FP, FN, la précision, le rappel et le F1, puis exporte les résultats sous forme de tableaux exploitables pour le rapport final.
