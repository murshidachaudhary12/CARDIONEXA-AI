import numpy as np
import cv2
from tensorflow.keras.models import load_model

model = load_model("model/heart_model.h5")

def preprocess_image(image):
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    return np.expand_dims(image, axis=0)

def predict_disease(image_array):
    processed = preprocess_image(image_array)
    prediction = model.predict(processed)[0][0]
    score = round((1 - prediction) * 100, 2)
    disease = "Arrhythmia" if score < 60 else "Normal"
    return score, disease
