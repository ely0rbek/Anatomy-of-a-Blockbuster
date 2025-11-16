import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast, os

csv_path="D:\python\BlockbusterDB\\movies_metadata.csv"
def parse_genres(x):
    if pd.isna(x): return []
    try:
        data = ast.literal_eval(x)
        if isinstance(data, list):
            return [d.get('name', '') for d in data if isinstance(d, dict)]
    except:
        return []
    return []


def plot_genre_avg_rating(csv_path):
    df = pd.read_csv(csv_path, low_memory=False)
    df['genres_parsed'] = df['genres'].apply(parse_genres)
    df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')
