import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast, os

csv_path="D:\python\Anatomy_of_Blockbuster\datasets\\movies_metadata.csv"
def parse_genres(x):
    if pd.isna(x): return []
    try:
        data = ast.literal_eval(x)
        if isinstance(data, list):
            return [d.get('name', '') for d in data if isinstance(d, dict)]
    except:
        return []
    return []


def plot_genre_avg_rating():
    df = pd.read_csv(csv_path, low_memory=False)
    df['genres_parsed'] = df['genres'].apply(parse_genres)
    df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')

    df = df.explode('genres_parsed').dropna(subset=['genres_parsed'])
    genre_stats = df.groupby('genres_parsed')['vote_average'].mean().sort_values(ascending=False)

    top = genre_stats.head(15)
    os.makedirs("plots", exist_ok=True)
    plt.figure(figsize=(10,6))
    plt.bar(top.index, top.values)
    plt.xticks(rotation=45, ha='right')
    plt.title("Top Genres by Average Rating")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.savefig("plots/genres_avg_rating.png")
    plt.show()

