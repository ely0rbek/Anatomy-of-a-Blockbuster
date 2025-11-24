import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from blockbuster_analysis.models import Parsing, csv_paths

def plot_budget_vs_revenue():
    csv_path=csv_paths()
    parsing=Parsing()

    df=pd.read_csv(csv_path.get_movies_path(),low_memory=False)
    df["budget"]=df['budget'].apply(parsing.parse_float)
    df['revenue']=df['revenue'].apply(parsing.parse_float)
    df=df[(df['budget']>0) & (df['revenue']>0)]

    x=np.log10(df['budget'])
    y=np.log10(df['revenue'])
    coef=np.polyfit(x,y,1)

    plt.figure(figsize=(8,6))
    plt.scatter(x, y, alpha=0.3, s=10)
    plt.plot(x, coef[0]*x + coef[1], color='red')
    plt.xlabel("log10(Budget)")
    plt.ylabel("log10(Revenue)")
    plt.title(f"Budget vs Revenue (log-log)\nSlope={coef[0]:.2f}")
    plt.tight_layout()
    # plt.savefig("plots/budget_vs_revenue.png")
    plt.show()

plot_budget_vs_revenue()


# ------------------- this is chart without log ------------------
    # x=df['budget']
    # y=df['revenue']
    # coef=np.polyfit(x,y,1)

    # plt.figure(figsize=(8,6))
    # plt.scatter(x, y, alpha=0.3, s=10)
    # plt.plot(x, coef[0]*x + coef[1], color='red')
    # plt.xlabel("log10(Budget)")
    # plt.ylabel("log10(Revenue)")
    # plt.title(f"Budget vs Revenue (log-log)\nSlope={coef[0]:.2f}")
    # plt.tight_layout()
    # plt.show()


