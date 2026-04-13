from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV file, converting numeric fields to float and id to int."""
    import csv
    
    print(f"Loading songs from {csv_path}...")
    songs = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields to float
            numeric_fields = ['energy', 'tempo_bpm', 'valence', 'danceability', 
                            'acousticness', 'instrumentalness', 'liveness']
            for field in numeric_fields:
                row[field] = float(row[field])
            
            # Convert id to int
            row['id'] = int(row['id'])
            
            # title, artist, genre, mood remain as strings
            songs.append(row)
    
    print(f"Loaded {len(songs)} songs.")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences; return (score, reasons) tuple."""
    score = 0.0
    reasons = []
    
    # Categorical matches (27.5 points total: genre halved to 12.5, mood 15)
    if song['genre'] == user_prefs['genre']:
        score += 12.5  # MODIFIED: Halved from 25 to test sensitivity
        reasons.append("genre match (+12.5)")
    
    if song['mood'] == user_prefs['mood']:
        score += 15
        reasons.append("mood match (+15)")
    
    # Numeric similarities with weights (51 points total: energy doubled to 16)
    numeric_features = {
        'energy': 16,  # MODIFIED: Doubled from 8 to test sensitivity
        'acousticness': 8,
        'instrumentalness': 8,
        'valence': 5,
        'danceability': 5,
        'liveness': 3
    }
    
    for feature, weight in numeric_features.items():
        user_value = user_prefs[feature]
        song_value = song[feature]
        similarity = 1 - abs(user_value - song_value)
        points = similarity * weight
        score += points
        reasons.append(f"{feature} similarity ({points:.1f}/{weight})")
    
    # Handle tempo separately (needs normalization: (bpm - 60) / 110)
    user_tempo = user_prefs['tempo_bpm']
    song_tempo = song['tempo_bpm']
    user_tempo_norm = (user_tempo - 60) / 110
    song_tempo_norm = (song_tempo - 60) / 110
    tempo_similarity = 1 - abs(user_tempo_norm - song_tempo_norm)
    tempo_points = tempo_similarity * 6
    score += tempo_points
    reasons.append(f"tempo_bpm similarity ({tempo_points:.1f}/6)")
    
    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, sort by score, and return top k recommendations."""
    # Score all songs using list comprehension and unpack the tuple
    scored_songs = [(song, *score_song(user_prefs, song)) for song in songs]
    
    # Sort by score (index 1) in descending order and return top k
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
