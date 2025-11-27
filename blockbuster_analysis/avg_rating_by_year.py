import pandas as pd
import matplotlib.pyplot as plt
from blockbuster_analysis.models import csv_paths

def plot_avg_rating_by_year():
    movies = pd.read_csv(csv_paths.csv_movies_path, low_memory=False)

    movies['release_date']=pd.to_datetime(movies['release_date'], errors='coerce')

    movies['year']=movies['release_date'].dt.year

    movies['vote_average'] = pd.to_numeric(movies['vote_average'], errors='coerce')

    # Filter valid years & ratings
    movies = movies[(movies['year'] >= 1950) & (movies['year'] <= 2022)]
    movies = movies[movies['vote_average'] > 0]

    # Average rating by year
    year_avg = movies.groupby('year')['vote_average'].mean()

    # Plot
    # plt.figure(figsize=(12, 5))
    plt.plot(year_avg.index, year_avg.values)
    plt.title("Average Rating by Year (1950–2022)")
    plt.xlabel("Year")
    plt.ylabel("Average Rating")
    plt.grid(True)
    plt.show()
