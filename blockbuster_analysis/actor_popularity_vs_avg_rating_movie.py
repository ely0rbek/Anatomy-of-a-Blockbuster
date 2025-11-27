import pandas as pd, ast
import matplotlib.pyplot as plt
import numpy as np
from blockbuster_analysis.models import csv_paths, Parsing

def plot_actor_popularity_vs_avg_rating_movie():

    movies = pd.read_csv(csv_paths.csv_movies_path, low_memory=False)
    credits = pd.read_csv(csv_paths.csv_credits_path, low_memory=False)

    # Clean movie IDs
    movies = movies[movies['id'].apply(lambda x: str(x).isdigit())]
    movies['id'] = movies['id'].astype(int)
    movies['vote_average'] = pd.to_numeric(movies['vote_average'], errors='coerce')

    movie_rating_map = dict(zip(movies['id'], movies['vote_average']))
    
    credits['cast'] = credits['cast'].apply(Parsing.safe_list_parse)

    actor_movies = {}
    for _, row in credits.iterrows():
        mid_raw = row['id']
        if str(mid_raw).isdigit():
            mid = int(mid_raw)
            for c in row['cast']:
                actor = c.get('name')
                if actor:
                    actor_movies.setdefault(actor, []).append(mid)

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



