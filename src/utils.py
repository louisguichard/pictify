""" This module is a set of helpers for all others modules """

LABELS = [
    "Art",
    "Barbecue",
    "Bathroom",
    "Beach",
    "Bedroom",
    "Beer",
    "Board Games",
    "Cleaning",
    "Coffee",
    "Cooking",
    "Flight",
    "France",
    "Garden",
    "Gym",
    "Hot",
    "Italy",
    "Japan",
    "Metro",
    "Movie",
    "Nature",
    "Party",
    "Piano",
    "Pool",
    "Rainy",
    "Reading",
    "Running",
    "Sport",
    "Train",
    "Traveling",
    "Working",
]


def from_url_to_embed(playlist_url):
    playlist_id = playlist_url.split("?")[0].split("/")[-1]
    return f"https://open.spotify.com/embed/playlist/{playlist_id}?utm_source=generator"
