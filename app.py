""" This module is to deisgn the streamlit app """

import json
import streamlit as st
from PIL import Image, ImageOps
from src.predict import predict
from src.utils import from_url_to_embed


with open("src/playlists.json") as f:
    playlists = json.load(f)


st.title("Pictify")
st.write("From pixels to music!")

uploaded_file = st.file_uploader("Take a photo!")

if uploaded_file:
    image = Image.open(uploaded_file)

    # Show image
    image = ImageOps.exif_transpose(image)
    st.image(image, width=300, caption="Your photo.")

    # Get predictions
    predictions = predict(image)

    # Show top-3
    st.dataframe(predictions.head(3))

    # Show best playlist
    st.components.v1.iframe(
        src=from_url_to_embed(playlists[predictions.index[0]]),
        height=352,
    )
