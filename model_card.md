# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMetric 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

This recommender is a classroom exploration tool designed to suggest songs based on a user's specific "vibe" (genre, mood, and energy). It assumes the user has clear preferences and is looking for songs within a small, curated catalog. It is not intended for real-world commercial use but rather to demonstrate how weighted scoring logic impacts discovery.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

The model uses a Weighted Scoring System. It looks at song attributes like genre, mood, and numerical values like energy, acousticness, and tempo.

Match Points: It gives a large point "bonus" if the song’s genre or mood exactly matches the user's preference.

Similarity Points: For numerical values like energy, it calculates the "gap" between the user's target and the song's actual value. The smaller the gap, the more points the song earns.

Final Ranking: It adds all these points together to create a score out of 100 and sorts the songs from highest to lowest.
---

## 4. Data  

The catalog consists of 18 songs. The dataset is skewed toward Lofi (16.7%) and Pop (11.1%), while other genres like Metal or Reggae only have one song each. The energy levels in the dataset are clustered between 0.28 and 0.94, meaning there is a complete lack of "ultra-chill" music below 0.28.
---

## 5. Strengths  

Where does your system seem to work well  

The system works very well for users with "mainstream" or "middle-of-the-road" tastes. If a user likes Lofi or Pop with moderate energy levels, the system provides several highly accurate and relevant matches that feel intuitive and correct.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The system suffers from a significant "Genre Filter Bubble" due to the high original weight (+25) for genre matches, which forces users into narrow categories and prevents cross-genre discovery. Furthermore, there is a "Neutrality Bias" in the energy gap calculation; because the dataset lacks songs with extreme values (below 0.28), users seeking very chill music are mathematically penalized compared to users with moderate preferences. Finally, the exact-match logic for moods creates a "Binary Limitation," where semantically similar moods like 'Chill' and 'Relaxed' receive no shared credit, leading to rigid and often repetitive recommendations.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested the system using three distinct profiles: "Lofi Study" (Low Energy/Lofi), "High-Energy Metal" (High Energy/Metal), and "Mainstream Pop" (Medium Energy/Pop). A surprising result was that the "Lofi Study" profile was significantly easier for the system to satisfy because 16.7% of the dataset is Lofi, whereas the "Metal" user was repeatedly suggested the same single song due to low dataset diversity. My experiment of halving the genre weight proved that the system can become more "vibe-focused," but it cannot fully overcome the underlying imbalance of the song catalog.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Dynamic Dataset Balancing: Add more songs to underrepresented genres to break the "single-song" trap.

Fuzzy Mood Matching: Instead of an "all or nothing" score for moods, I would create groups (e.g., 'Chill' and 'Relaxed' share points) to improve variety.

Non-Linear Scoring: Adjust the energy gap math so it doesn't unfairly punish users who want extreme "edge case" music.
---

## 9. Personal Reflection  

A few sentences about your experience.  

My biggest learning moment was discovering the "Extreme Value Penalty"—realizing that my math accidentally punished people with strong tastes just because the data didn't perfectly match their 0.1 or 0.9 energy preference. AI tools were incredibly helpful for generating additional CSV data and explaining the math behind the scores, but I had to double-check the AI's logic when it suggested weight changes that would have made the genre match too powerful. I was surprised by how a few lines of addition and subtraction can make a computer "feel" like it understands my musical taste, even though it's just calculating distances between numbers. This project made me realize that the "algorithms" we complain about on TikTok or Spotify are essentially just a series of human-weighted decisions.
