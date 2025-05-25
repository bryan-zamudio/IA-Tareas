from tensorflow.keras.preprocessing.image import ImageDataGenerator

ruta = r"IA\Expresiones\Face Recognition Images\FER2013\train"

# Definimos el generador
datagen = ImageDataGenerator(
    rescale=1./255,                 # Reescalado de los valores de cada pixel a un rango de 0-1
    rotation_range=20,              # Rotación de -20° a 20°
    zoom_range=0.2,                 # Zoom de -20% a 20%
    brightness_range=[0.6, 1.4],    # Cambio de brillo de 60% a 140%
    horizontal_flip=True,           # Volteo horizontal
    fill_mode='nearest'             # Relleno de píxeles tomando el más cercano
)

# Creamos el generador
train_generator = datagen.flow_from_directory(
    ruta,
    target_size=(96, 96),
    batch_size=32,  
    class_mode='categorical'        # Etiquetamos cada imagen según la carpeta en la que esté
)
