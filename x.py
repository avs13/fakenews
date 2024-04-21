from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import load

# Cargar el modelo entrenado
model = load('modelo_entrenado.joblib')

# Leer la noticia del archivo
with open('noticia.txt', 'r') as archivo:
    noticia_usuario = archivo.read()

# Cargar el vectorizador TF-IDF entrenado
vectorizer = load('vectorizer.joblib')

# Vectorizar la noticia
noticia_vectorizada = vectorizer.transform([noticia_usuario])

# Predecir con el modelo de regresión logística
prediccion = model.predict(noticia_vectorizada)

# Interpretar y mostrar el resultado basado en un umbral
umbral = 0.5
if prediccion >= umbral:
    print(f"La noticia es probablemente FALSA con un valor de predicción de {prediccion[0]}")
else:
    print(f"La noticia es probablemente VERDADERA con un valor de predicción de {prediccion[0]}")