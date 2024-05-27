"""This module is to design the streamlit app"""

import streamlit as st
from PIL import Image, ImageOps
from src.predict import predict
from src.utils import from_url_to_embed, load_example
from data.constants import PHOTO_EXAMPLES, PLAYLIST_URLS


st.set_page_config(page_title="Pictify", page_icon="🎶")
st.image("logo.png", use_column_width=True)
st.write(
    "Take a photo of what's around you and let Pictify find the perfect playlist for you!"
)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def get_playlist(image):
    # Show image
    image = ImageOps.exif_transpose(image)
    st.image(image, width=300, caption="Your photo.")

    # Get predictions
    predictions = predict(image)

    # Show best playlist
    st.components.v1.iframe(
        src=from_url_to_embed(PLAYLIST_URLS[predictions.index[0]]),
        height=352,
    )

    # How it works
    with st.expander("How it works?"):
        how_it_works = """
        Pictify is based on a cutting-edge Deep Learning model called EfficientNet. 
        It's a convolutional neural network specially designed for image processing. 
        It has been trained (or more precisely 'fine-tuned') to recognize 
        a large number of topics such as cooking, running or traveling. 
        This is what enables Pictify to make sense of your picture 
        and recommend the perfect playlist for the situation!
        """
        st.write(how_it_works)
        st.write("Here are the themes identified in your photo:")
        st.dataframe(predictions.head(3))  # show top-3
        st.write(
            "Find out more on the [Github](https://github.com/louisguichard/pictify) repository!"
        )


uploaded_file = st.file_uploader(
    "Take a snap!", help="Photos are not saved.", type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    get_playlist(image)
else:
    choice = st.selectbox("Or choose an example...", PHOTO_EXAMPLES.keys())
    if choice != "No choice":
        image = load_example(choice)
        get_playlist(image)
