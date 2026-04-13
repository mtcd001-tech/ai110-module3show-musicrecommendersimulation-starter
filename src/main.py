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

    recommendations = recommend_songs(user_prefs, songs, k=5)

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
