# TuneAI - AI Music Recommendation System

TuneAI is a simple AI-powered music recommendation system built using Python and Streamlit. It recommends songs similar to the one selected by the user using a content-based filtering approach with machine learning.

The project demonstrates how Natural Language Processing (NLP) techniques and the Nearest Neighbors algorithm can be used to build a basic recommendation engine.

## Features

- Recommend similar songs instantly
- Simple and clean user interface
- Content-based recommendation system
- Displays artist, album type, popularity, and duration
- Fast and lightweight Streamlit application

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- CountVectorizer
- Nearest Neighbors

## Project Structure

```
TuneAI/
│
├── tune.py
├── recommendation.py
├── spotify_data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Misbah430/DecodeLabs-AI-music-recommendation-system.git
```

### 2. Navigate to the project folder

```bash
cd DecodeLabs-AI-music-recommendation-system
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run tune.py
```

The application will open automatically in your browser.

## How It Works

1. The Spotify dataset is loaded and cleaned.
2. Artist names and album types are combined into text features.
3. CountVectorizer converts the text into numerical vectors.
4. A Nearest Neighbors model is trained on these vectors.
5. When a user selects a song, the model finds and recommends the most similar songs.

## Dataset

The dataset contains information such as:

- Song Name
- Artist
- Album Type
- Popularity
- Duration

## Future Improvements

- Add genre-based recommendations
- Integrate Spotify API
- Display album cover images
- Play song previews
- Add search by artist
- Improve recommendation accuracy using TF-IDF


GitHub: https://github.com/Misbah430

## License

This project is created for educational purposes and learning machine learning concepts.
