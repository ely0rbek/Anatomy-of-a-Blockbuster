import pandas as pd 
import matplotlib.pyplot as plt
from blockbuster_analysis.models import csv_paths

def plot_revenue_by_year():
    csv_path=csv_paths()
    df=pd.read_csv(csv_path.get_movies_path(),low_memory=False)
    df['revenue']= list(map(float,df["revenue"]))
    df['release_date']=pd.to_datetime(df['release_date'], errors='coerce')

    df['year']=df['release_date'].dt.year

    static_data=df.groupby('year')['revenue'].mean().dropna()

    plt.bar(static_data.index, static_data.values)
    plt.title("Average Revenue by Year")
    plt.xlabel("Year")
    plt.ylabel("Average Revenue")
    # plt.savefig("plots/avg_revenue_by_year.png")
    plt.show()

plot_revenue_by_year()
