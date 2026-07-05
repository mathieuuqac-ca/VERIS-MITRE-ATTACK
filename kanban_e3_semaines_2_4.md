# Kanban E3 — Semaines 2 et 4

## DONE

### Étude du besoin E3
- Le rôle E3 correspond à la partie systèmes et intégration.
- Les deux livrables principaux sont :
  - pipeline VCDB → normalisation → CSV/JSON ;
  - wrapper API avec rate limiting, retries et parsing JSON.

### Structure VS Code
- Création d'un dossier projet propre.
- Ajout d'une configuration `.vscode`.
- Ajout d'un `requirements.txt`.
- Ajout d'un `.env.example`.
- Ajout de `.gitattributes` pour Git LFS.

## IN PROGRESS

### Pipeline semaine 2
- Lecture récursive des fichiers JSON VCDB.
- Extraction des champs VERIS : actor, action, asset, attribute.
- Recherche d'un texte narratif ou résumé d'incident.
- Export CSV et JSONL.
- Logs d'erreurs.

### Wrapper semaine 4
- Lecture des incidents propres.
- Construction du prompt.
- Mode mock sans API.
- Validation des sorties JSON.
- Export des prédictions.

## TODO

### Tests avec la vraie VCDB
- Cloner `https://github.com/vz-risk/VCDB`.
- Lancer l'ingestion sur un échantillon.
- Vérifier les colonnes produites.

### Tests API réels
- Ajouter une clé API dans `.env`.
- Lancer le wrapper sur 5 incidents.
- Vérifier les sorties dans `outputs/predictions_zero_shot.jsonl`.

### Améliorations possibles
- Ajouter un mapping CTID comme vérité terrain.
- Ajouter des statistiques sur les champs VERIS extraits.
- Ajouter une base vectorielle pour la phase RAG.
