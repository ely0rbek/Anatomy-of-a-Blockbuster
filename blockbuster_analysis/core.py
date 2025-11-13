import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("D:\python\BlockbusterDB\\movies_metadata.csv",low_memory=False)

df['revenue']= list(map(float,df["revenue"]))

df['release_date']=pd.to_datetime(df['release_date'], errors='coerce')



def show_plot_revenue_by_year():
    df['year']=df['release_date'].dt.year

    static_data=df.groupby('year')['revenue'].mean().dropna()

    plt.bar(static_data.index, static_data.values)
    plt.title("Average Revenue by Year")
    plt.xlabel("Year")
    plt.ylabel("Average Revenue")

    plt.show()



