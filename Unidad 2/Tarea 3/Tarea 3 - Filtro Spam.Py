import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#nltk.download("stopwords")
#nltk.download("punkt")
#nltk.download("wordnet")

# Cargar dataset
data = pd.read_csv("spam_assassin.csv")

# Lematizador para normalizar texto
lematizador = WordNetLemmatizer()
# Set con las stopwords en inglés
stop_words = set(stopwords.words('english'))

def preProcesar(texto):
    #Normaliza el texto: minúsculas, elimina caracteres especiales, lematiza y filtra stopwords.
    texto = texto.str.lower()
    texto = texto.str.replace("[^a-z0-9]", " ")
    texto = texto.str.split()
    texto = texto.apply(lambda x: " ".join([lematizador.lemmatize(word) for word in x if word not in stop_words]))
    return texto

# Aplicar preprocesamiento a los correos del dataset
data["text"] = preProcesar(data["text"])

# Extracción de características con TF-IDF
vectorizador = TfidfVectorizer()
caracteristicas = vectorizador.fit_transform(data["text"])

# Etiquetas (1 = spam, 0 = no spam)
y = data["target"].values

# Calcular P(Spam) y P(No Spam)
P_spam = np.sum(y) / len(y)
P_no_spam = 1 - P_spam

# Array booleano para filtrar por spam y no spam
spam_arr = (y == 1)
no_spam_arr = (y == 0)

# Array donde guardar la frecuencia, Frecuencia = Suma de las caracteristicas de todos los correos spam
frecuencia_spam = np.sum(caracteristicas[spam_arr], axis=0)
# Frecuencia = Suma de las caracteristicas de todos los correos no spam
frecuencia_no_spam = np.sum(caracteristicas[no_spam_arr], axis=0)

# Conteo total de características de palabras
total_spam = frecuencia_spam.sum()
total_no_spam = frecuencia_no_spam.sum()

# Hacemos una comparacion del valor de cada palabra con el valor total de todas las palabras
# Probabilidades de características dado spam (P(Caracteristicas|Spam) = Frecuencia de la palabra en spam / Total de palabras)
P_caracteristicas_spam = frecuencia_spam / total_spam
# Probabilidades de características dado no spam (P(Caracteristicas|No Spam))
P_caracteristicas_no_spam = frecuencia_no_spam / total_no_spam

def clasificar(email):
    # Preprocesamos el texto del nuevo correo
    email_proc = preProcesar(pd.Series([email]))
    # Vectorizamos su texto
    email_tfidf = vectorizador.transform(email_proc)
    
    # Multiplicamos la importancia de cada palabra por las características de spam y no spam de cada una
    P_caracteristicas_spam_email = email_tfidf @ P_caracteristicas_spam.T
    P_caracteristicas_no_spam_email = email_tfidf @ P_caracteristicas_no_spam.T
    
    # Aplicamos la fórmula de Bayes
    P_spam_caracteristicas = (P_spam * P_caracteristicas_spam_email) / (
        (P_spam * P_caracteristicas_spam_email) + (P_no_spam * P_caracteristicas_no_spam_email) + 1e-100) # Sumamos una cantidad pequeña para que no de error /0
    
    # Regresa Spam si las probabilidades de ser spam son mayores a 0.3, en caso contrario regresa No Spam
    return "Spam" if P_spam_caracteristicas > 0.3 else "No Spam"

# Evaluación del modelo
# Procesamos cada correo del dataset con la funcion clasificar
predicciones = [clasificar(email) for email in data["text"]]
# Guardamos cada prediccion que hizo en un array
clasificaciones = np.array([1 if p == "Spam" else 0 for p in predicciones])

# Impresión de estadísticas
print("Cantidad de correos: ", len(y))
print("Cantidad de correos spam: ", np.sum(y))
print("Cantidad de correos no spam: ", len(y) - np.sum(y))
print("\nCantidad de correos detectados como spam: ", np.sum(clasificaciones == 1))
print("Cantidad de correos detectados como no spam: ", np.sum(clasificaciones==0))
print("\nCantidad de correos detectados correctamente: ",np.sum(clasificaciones == y))
print("Cantidad de correos detectados correctamente como spam: ",np.sum((clasificaciones == 1) & (y == 1)))
print("Cantidad de correos detectados correctamente como no spam: ", np.sum((clasificaciones == 0) & (y ==0)))

# Comparamos cuantos correos clasificó correctamente
precision = np.sum(clasificaciones == y) / len(y)
# Comparamos cuantos spam clasificó correctamente
recuperacion = np.sum((clasificaciones == 1) & (y == 1)) / np.sum(y)

print(f"\nPrecisión: {precision*100:.3f}%")
print(f"Recuperación: {recuperacion*100:.3f}%")
