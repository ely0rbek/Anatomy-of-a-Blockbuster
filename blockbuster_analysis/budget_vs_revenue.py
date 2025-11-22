import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def check_float(x):
    try:
        return float(str(x).replace(',', '').replace('$', ''))
    except:
        return np.nan
    

def plot_budget_vs_revenue():
    csv_path="D:\python\Anatomy_of_Blockbuster\datasets\\movies_metadata.csv"
    df=pd.read_csv(csv_path,low_memory=False)
    df["budget"]=df['budget'].apply(check_float)
    df['revenue']=df['revenue'].apply(check_float)
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


