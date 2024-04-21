from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
# Cargar el modelo entrenado

def model(news):
    model = load('model.joblib')
    vectorizer = load('vectorizer.joblib')
    # Vectorizar la noticia
    noticia_vectorizada = vectorizer.transform([news])

    # Predecir con el modelo de regresión lineal
    prediccion = model.predict(noticia_vectorizada)
    print(prediccion)
    return prediccion
    ## Interpretar y mostrar el resultado basado en un umbral
    #umbral = 0.5
    #if prediccion >= umbral:
    #    print(f"La noticia es probablemente FALSA con un valor de predicción de {prediccion[0]}")
    #else:
    #    print(f"La noticia es probablemente VERDADERA con un valor de predicción de {prediccion[0]}")
    ## Evaluar el modelo
#
    #accuracy = accuracy_score(y_test, y_pred)
    #print(f'Accuracy: {accuracy * 100:.2f}%')

