Téléchargez le fichier predict.py sur votre ordinateur.

Téléchargez les fichiers de modèle NLP entraînés (trained_Nlp_model.pkl ettrained_Nlp_vectorizer.pkl) et placez-les dans le même répertoire que le fichier predict.py.

Ouvrez une invite de commande ou un terminal et accédez au répertoire où se trouve le fichier predict.py.

Dans l'invite de commande ou le terminal, lancez le fichier predict.py avec la commande : python predict.py <equipment_name>, où <equipment_name> est le nom de l'équipement que vous souhaitez classer en français.

Par exemple, si vous souhaitez classer un équipement nommé "Réacteur", vous exécuterez la commande suivante :

python predict.py 'Réacteur'

Le programme affichera les trois meilleures classes prédites et leurs scores de confiance. Si le score de confiance est inférieur à 0,5, cela signifie que le modèle n'est pas sûr de sa prédiction et renverra Aucun.

Pour avoir les metriques de ce modéle executez le fichier predict.ipynb .

Remarque : Assurez-vous que les packages requis sont installés, tels que numpy, pandas, nltk et scikit-learn, car ils sont utilisés dans le fichier predict.py en utiliant la commande pip install requirements.txt .