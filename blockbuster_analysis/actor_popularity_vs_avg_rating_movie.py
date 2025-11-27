import pandas as pd, ast
import matplotlib.pyplot as plt
import numpy as np
from models import Parsing, csv_paths

# Load data

def plot_actor_popularity_vs_avg_rating_movie():
    # parsing=Parsing() 

    credits = pd.read_csv(csv_paths.csv_credits_path, low_memory=False)
    movies = pd.read_csv(csv_paths.csv_movies_path, low_memory=False)

    # Clean movie IDs
    movies = movies[movies['id'].apply(lambda x: str(x).isdigit())]
    movies['id'] = movies['id'].astype(int)
    movies['vote_average'] = pd.to_numeric(movies['vote_average'], errors='coerce')

    # Build dictionary for fast movie → rating lookup
    movie_rating_map = dict(zip(movies['id'], movies['vote_average']))

    # Safe JSON parsing
    def safe_parse(x):
        try:
            r = ast.literal_eval(x)
            return r if isinstance(r, list) else []
        except:
            return []

    credits['cast'] = credits['cast'].apply(safe_parse)

    # Build actor → list of movie IDs
    actor_movies = {}
    for _, row in credits.iterrows():
        mid_raw = row['id']
        if str(mid_raw).isdigit():
            mid = int(mid_raw)
            for c in row['cast']:
                actor = c.get('name')
                if actor:
                    actor_movies.setdefault(actor, []).append(mid)

    # Compute actor popularity + average rating
    actor_stats = []
    for actor, mids in actor_movies.items():
        ratings = [movie_rating_map[m] for m in mids if m in movie_rating_map]
        ratings = [r for r in ratings if pd.notna(r)]
        if ratings:
            actor_stats.append({
                "Actor": actor,
                "Popularity": len(mids),
                "Average_Rating": np.mean(ratings)
            })

    df = pd.DataFrame(actor_stats)

    # Linear regression (Popularity → Rating)
    x = df["Popularity"]
    y = df["Average_Rating"]
    m, b = np.polyfit(x, y, 1)

    # Plot
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, alpha=0.4)
    plt.plot(x, m*x + b)
    plt.xlabel("Popularity")
    plt.ylabel("Average_Rating")
    plt.title("Regression: Actor Popularity → Average Rating")
    plt.grid(True)
    plt.show()


plot_actor_popularity_vs_avg_rating_movie()
