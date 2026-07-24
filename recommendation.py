import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

# -----------------------------
# Load Dataset
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "spotify_data.csv")

df = pd.read_csv(DATA_PATH, encoding="latin1")

# -----------------------------
# Keep Required Columns
# -----------------------------

df = df[
    [
        "Song Name",
        "Artists",
        "Album Type",
        "Popularity",
        "Duration",
    ]
].copy()

# -----------------------------
# Clean Dataset
# -----------------------------

df.dropna(inplace=True)
df.drop_duplicates(subset="Song Name", inplace=True)
df.reset_index(drop=True, inplace=True)

# -----------------------------
# Create Tags
# -----------------------------

df["tags"] = (
    df["Artists"].fillna("")
    + " "
    + df["Album Type"].fillna("")
)

# -----------------------------
# Convert Text into Vectors
# -----------------------------

cv = CountVectorizer(stop_words="english")

vectors = cv.fit_transform(df["tags"])

# -----------------------------
# Train Model
# -----------------------------

model = NearestNeighbors(
    metric="cosine",
    algorithm="brute",
    n_neighbors=6
)

model.fit(vectors)

# -----------------------------
# Song List
# -----------------------------

def get_song_list():
    return sorted(df["Song Name"].tolist())

# -----------------------------
# Recommendation Function
# -----------------------------

def recommend(song_name):

    matches = df.index[df["Song Name"] == song_name].tolist()

    if not matches:
        return []

    idx = matches[0]

    distances, indices = model.kneighbors(vectors[idx:idx + 1])

    recommendations = []

    for distance, i in zip(distances[0][1:], indices[0][1:]):

        similarity = round((1 - distance) * 100, 2)

        recommendations.append(
            {
                "Song": df.loc[i, "Song Name"],
                "Artist": df.loc[i, "Artists"],
                "Album": df.loc[i, "Album Type"],
                "Popularity": df.loc[i, "Popularity"],
                "Duration": df.loc[i, "Duration"],
                "Similarity": similarity,
            }
        )

    return recommendations