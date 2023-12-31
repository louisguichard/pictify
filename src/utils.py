""" This module is a set of helpers for all others modules """

from PIL import Image
import streamlit as st
from data.constants import PHOTO_EXAMPLES


@st.cache_data(show_spinner=False)
def load_example(choice):
    photo = PHOTO_EXAMPLES[choice]
    image = Image.open("data/examples/" + photo)
    return image


def from_url_to_embed(playlist_url):
    playlist_id = playlist_url.split("?")[0].split("/")[-1]
    return f"https://open.spotify.com/embed/playlist/{playlist_id}?utm_source=generator"
