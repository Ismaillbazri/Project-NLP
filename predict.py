import sys
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import pickle

def predict(equipment_name):   

    # Récupération de fichiers enregistrés 

    with open('trained_Nlp_vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

    with open('trained_Nlp_model.pkl', 'rb') as file1:
        clf = pickle.load(file1)

    # Faire les transformations nécessaires sur le nom à normaliser

    stemmer=SnowballStemmer('french')
    tokens = word_tokenize(equipment_name.lower())
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    preprocessed_name = ' '.join(stemmed_tokens)
    X = vectorizer.transform([preprocessed_name])
    # Géneration de la liste des tuples

    predictions = [(label, prob) for label, prob in zip(clf.classes_, clf.predict_proba(X)[0])]
    predictions.sort(key=lambda x: x[1], reverse=True)

    predictions = predictions[:3] # Choix de prendre que les trois premiéres classes

    # Calculer la plus grande probabilité 
    
    confidence = clf.predict_proba(X).max()

    if confidence < 0.5:
        return None
    else:
        return predictions

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python predict.py <equipment_name>")
    else:
        equipment_name = ' '.join(sys.argv[1:])
        result = predict(equipment_name)
        if result is None:
            print("No prediction found.")
        else:
            print("-------------------------------------------")
            for prediction in result:
                print(f"Predicted Name: {prediction[0]}, Confidence: {prediction[1]}",)