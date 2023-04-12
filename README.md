<h1>README</h1>
Projet de normalisation des noms des équipements

<h2>Introduction</h2>
L'objectif de ce projet est de créer un modèle qui peut normaliser le nom de tout équipement dans une usine. Les variations dans la façon dont les noms des équipements sont écrits ou étiquetés peuvent entraîner des erreurs de communication ou des problèmes de maintenance. Avec un modèle de standardisation des noms d'équipements, les travailleurs de l'usine peuvent être sûrs qu'ils parlent tous de la même chose, quel que soit le fabricant ou la variation dans la façon dont les noms sont écrits.

<h2>Base de données</h2>
Le jeu de données utilisé se trouve dans le dossier de données. Il contient 1 fichier : extract_normalised_name_fr_training_data.xlsx qui contient 2 colonnes : désignation_fr et normalised_name.

La colonne designation_fr contient le nom de n'importe quel équipement dans une usine.

La colonne normalised_name contient le nom de l'équipement normalisé.
<h2>Méthodologie</h2>

Le projet a été développé en Python. Les bibliothèques suivantes ont été utilisées :

pandas
scikit-apprendre
nltk

Un pipeline de prétraitement a été utilisé pour préparer les données pour la modélisation. Les étapes comprennent :

Tokénisation des noms d'équipements<br>
Stemming des jetons pour les réduire à leur forme de base<br>
Vectorisation des jetons à tige à l'aide de la vectorisation TF-IDF<br>
Entraînement d'un modèle de régression logistique sur les données vectorisées<br>

<h2>Livrables</h2>
Le projet est livré dans ce dépôt git. Il comprend les fichiers suivants :

-predict.py : un script python qui contient une fonction pour normaliser les noms d'équipement.<br>
-predict.ipynb : un fichier python qui contient l'entrainement du modéle et ses metrics (précision, recall , accuracy, F1-score).
-trained_Nlp_model.pkl : un fichier pickle contenant le modèle de régression logistique formé.
-trained_Nlp_vectorizer.pkl : un fichier pickle contenant le vectoriseur formé.
-INSTRUCTIONS.md 

Le fichier predict.py contient la fonction predict qui prend une chaîne en paramètre (le nom de l'équipement) et retourne une liste de tuple (nom prédit, confiance) ou None si le nom n'est pas reconnu.
<h2>Usage</h2>

Pour utiliser le script predict.py, suivez ces instructions :

Assurez-vous que les bibliothèques requises sont installées (pandas, scikit-learn, nltk).<br>
Téléchargez le jeu de données à partir du dossier de données.<br>
Placez les fichiers predict.py,trained_Nlp_model.pkl ettrained_Nlp_vectorizer.pkl dans le même répertoire.<br>
Ouvrez une fenêtre de terminal et accédez au répertoire où se trouvent les fichiers.<br>
Exécutez la commande suivante : python predict.py <equipment_name><br>
Remplacez <equipment_name> par le nom de l'équipement que vous souhaitez normaliser.<br>
Si le nom est reconnu, la fonction renverra une liste de tuples, chacun contenant le nom prédit et le score de confiance. Si le nom n'est pas reconnu, la fonction renverra Aucun.<br>
<h2>Métriques du modéle</h2>
![image](https://user-images.githubusercontent.com/88779439/231577793-db1fb45c-e0ac-430f-b39a-996031f7e50a.png)
