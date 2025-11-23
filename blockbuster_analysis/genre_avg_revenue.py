import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from models import csv_paths, Parsing

def plot_genre_avg_revenue():
    csv_path=csv_paths()
    parsing=Parsing()

    df=pd.read_csv(csv_path.get_movies_path(),low_memory=False)

    df['genres_parsed']=df['genres'].apply(parsing.parse_genres)
    df['revenue']=df['revenue'].apply(parsing.check_float)

    df = df.explode('genres_parsed').dropna(subset=['genres_parsed'])
    genre_stats = df.groupby('genres_parsed')['revenue'].mean().sort_values(ascending=False)
    
    top_15_genre = genre_stats.head(15)
    plt.figure(figsize=(10,6))
    plt.bar(top_15_genre.index, top_15_genre.values)
    plt.yscale('log')
    plt.xticks(rotation=45, ha='right')
    plt.title("Top Genres by Average Revenue")
    plt.ylabel("Average Revenue")
    plt.tight_layout()
    # plt.savefig("plots/genres_avg_revenue.png")
    plt.show()


plot_genre_avg_revenue()

