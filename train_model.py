import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from joblib import dump

df = pd.read_csv('train.csv')

# Preprocesamiento básico
# Eliminar filas con valores nulos
df.dropna(inplace=True)

X = df['text']  
y = df['label']  

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorizar el texto
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Entrenar un modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Predecir etiquetas para el conjunto de prueba
y_pred = model.predict(X_test)
dump(model, 'model.joblib')
dump(vectorizer, 'vectorizer.joblib')