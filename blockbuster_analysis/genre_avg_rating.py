import pandas as pd
import matplotlib.pyplot as plt
from blockbuster_analysis.models import Parsing,csv_paths


def plot_genre_avg_rating():
    csv_path=csv_paths()
    parsing=Parsing()

    df = pd.read_csv(csv_path.get_movies_path(), low_memory=False)

    df['genres_parsed'] = df['genres'].apply(parsing.parse_genres)

    df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')

    df = df.explode('genres_parsed').dropna(subset=['genres_parsed'])
    genre_stats = df.groupby('genres_parsed')['vote_average'].mean().sort_values(ascending=False)

    top = genre_stats.head(15)
    plt.figure(figsize=(10,6))
    plt.bar(top.index, top.values)
    plt.xticks(rotation=45, ha='right')
    plt.title("Top Genres by Average Rating")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    # plt.savefig("plots/genres_avg_rating.png")
    plt.show()

