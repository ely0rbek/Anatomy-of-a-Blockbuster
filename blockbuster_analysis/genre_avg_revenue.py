import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast


def parse_genre(x):
    if pd.isna(x): 
        return []
    if isinstance(x,str):
        data=ast.literal_eval(x)
        if isinstance(data,list):
            return [d.get('name','') for d in data if isinstance(d, dict)]
    return []

def check_float(x):
    if pd.isna(x):
        return 0
    return float(str(x).replace(',','').replace('$',''))


def plot_genre_revenue():
    csv_path="D:\python\Anatomy_of_Blockbuster\datasets\\movies_metadata.csv"
    df=pd.read_csv(csv_path,low_memory=False)
    df['genres_parsed']=df['genres'].apply(parse_genre)
    df['revenue']=df['revenue'].apply(check_float)

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


