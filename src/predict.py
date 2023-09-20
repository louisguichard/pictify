""" This module is for getting predictions from the classification model """

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.applications.efficientnet_v2 import preprocess_input
from src.utils import LABELS


model = tf.keras.models.load_model("./models/EfficientNetV2S.h5")


def preprocess_image(image):
    image_resized = image.resize((300, 300))
    image_array = img_to_array(image_resized)
    image_array = np.expand_dims(image_array, axis=0)
    processed_image = preprocess_input(image_array)
    return processed_image


def predict(image):
    # Predict
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)[0]

    # Format output
    output = pd.DataFrame(predictions, index=LABELS, columns=["Probability"])
    output = output.sort_values(by="Probability", ascending=False)

    return output
