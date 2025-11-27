import pandas as pd
import matplotlib.pyplot as plt
from blockbuster_analysis.models import csv_paths

def plot_movie_count_by_year():
    movies = pd.read_csv(csv_paths.csv_movies_path, low_memory=False)

    movies['release_date']=pd.to_datetime(movies['release_date'], errors='coerce')

    movies['year']=movies['release_date'].dt.year

    movies['vote_average'] = pd.to_numeric(movies['vote_average'], errors='coerce')

    movies = movies[(movies['year'] >= 1950) & (movies['year'] <= 2022)]

    year_count = movies.groupby('year')['vote_average'].count()

    plt.plot(year_count.index, year_count.values)
    plt.title("Number of Movies Released per Year (1950–2022)")
    plt.xlabel("Year")
    plt.ylabel("Movie Count")
    plt.grid(True)
    plt.show()


