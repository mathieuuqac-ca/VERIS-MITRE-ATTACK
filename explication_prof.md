# Explication de la contribution E3

Pour la semaine 2, j'ai préparé un pipeline de données permettant de lire les fichiers JSON
de la VCDB, d'extraire les champs VERIS principaux, de normaliser les incidents et
d'exporter les résultats dans deux formats : CSV et JSONL.

Le CSV sert à l'analyse rapide et à la vérification manuelle. Le JSONL est plus adapté
aux appels LLM, car chaque ligne correspond à un incident indépendant.

J'ai aussi préparé la configuration Git LFS avec `.gitattributes`, afin de pouvoir versionner
les données volumineuses sans les stocker directement dans Git.

Pour la semaine 4, j'ai préparé un wrapper d'appels API. Il lit le fichier JSONL généré en
semaine 2, construit un prompt zéro-shot, appelle le modèle LLM, applique un délai entre les
requêtes pour limiter le rate limiting, relance automatiquement en cas d'erreur temporaire et
valide que la réponse respecte un schéma JSON structuré.

Le wrapper contient aussi un mode `--mock`, qui permet de tester tout le pipeline sans clé API
et sans consommer d'appels payants. Cela permet de vérifier la reproductibilité du code avant
d'utiliser un vrai modèle.
