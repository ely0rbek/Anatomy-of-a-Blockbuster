import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from models import Parsing, csv_paths

def plot_revenue_by_year():
    csv_path=csv_paths()
    parsing=Parsing()

    df=pd.read_csv(csv_path.get_movies_path(),low_memory=False)
    df['revenue']=df['revenue'].apply(parsing.check_float)
    df['release_date']=pd.to_datetime(df['release_date'],errors='coerce')
    df['year']=df['release_date'].dt.year

    stats=df.groupby('year')['revenue'].mean().dropna()

    plt.figure(figsize=(10,5))
    plt.plot(stats.index, stats.values, marker='o')
    plt.title("Average Revenue by Year")
    plt.xlabel("Year")
    plt.ylabel("Average Revenue (USD)")
    plt.grid(True)
    plt.tight_layout()
    # plt.savefig("plots/avg_revenue_by_year.png")
    plt.show()

plot_revenue_by_year()
