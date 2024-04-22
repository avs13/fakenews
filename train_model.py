import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
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

# Implementación del modelo SVM
model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train)

# Predecir etiquetas para el conjunto de prueba
y_pred = model.predict(X_test)
dump(model, 'model.joblib')
dump(vectorizer, 'vectorizer.joblib')

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
# Accuracy: 96.17%
