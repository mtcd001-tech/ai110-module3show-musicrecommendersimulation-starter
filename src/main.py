"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs



def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.40,
        "tempo_bpm": 78,
        "valence": 0.60,
        "danceability": 0.47,
        "acousticness": 0.80,
        "instrumentalness": 0.65,
        "liveness": 0.05,
    }

    # ADVERSARIAL PROFILE 1: Contradictory Acoustic + Electronic Signature
    adversarial_1 = {
        "genre": "synthwave",  # Electronic genre
        "mood": "confused",     # Non-existent mood in dataset
        "energy": 0.95,         # Very high energy
        "tempo_bpm": 45,        # Below normalized range (60-170); extreme low
        "valence": 0.05,        # Contradicts high energy (valence usually correlates)
        "danceability": 0.92,   # Very danceable
        "acousticness": 0.95,   # Very acoustic (conflicts with synthwave)
        "instrumentalness": 0.95,  # Highly instrumental (limits vocal tracks)
        "liveness": 0.02,       # Almost fully studio (conflicts with liveness)
    }

    # ADVERSARIAL PROFILE 2: Out-of-Dataset Boundaries
    adversarial_2 = {
        "genre": "metal",       # Genre not in dataset
        "mood": "aggressive",   # Mood not in dataset
        "energy": 1.0,          # Maximum edge (should score 0 similarity with most songs)
        "tempo_bpm": 210,       # Beyond dataset max (~152 BPM)
        "valence": 0.0,         # Minimum edge
        "danceability": 1.0,    # Maximum edge
        "acousticness": 0.0,    # Minimum edge (fully electronic)
        "instrumentalness": 0.5,
        "liveness": 1.0,        # Maximum live recording preference
    }

    # ADVERSARIAL PROFILE 3: Impossible Neutrality (All Extremes)
    adversarial_3 = {
        "genre": "lofi",        # Exists in dataset
        "mood": "focused",      # Exists in dataset
        "energy": 0.0,          # Minimum (contradicts focused work)
        "tempo_bpm": 180,       # Very fast (contradicts lofi chill vibe)
        "valence": 1.0,         # Maximum positivity
        "danceability": 0.0,    # Not danceable at all
        "acousticness": 1.0,    # Fully acoustic
        "instrumentalness": 0.0,  # Requires vocals only
        "liveness": 0.5,        # Perfectly neutral
    }
    recommendations = recommend_songs(adversarial_3, songs, k=5)

    print("\n" + "="*70)
    print("TOP MUSIC RECOMMENDATIONS FOR YOU".center(70))
    print("="*70)
    
    for rank, rec in enumerate(recommendations, 1):
        song, score, reasons = rec
        print(f"\n#{rank} - {song['title']} by {song['artist']}")
        print(f"    Score: {score:.1f}/100")
        print("    Why:")
        for reason in reasons:
            print(f"      • {reason}")
        print("-" * 70)


if __name__ == "__main__":
    main()
