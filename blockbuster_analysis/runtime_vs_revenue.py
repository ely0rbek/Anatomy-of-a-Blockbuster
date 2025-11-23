import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from blockbuster_analysis.models import Parsing, csv_paths

def plot_runtime_vs_revnue():
    csv_path=csv_paths()
    parsing=Parsing()

    df=pd.read_csv(csv_path.get_movies_path(),low_memory=False)

    df['runtime']=pd.to_numeric(df['runtime'],errors='coerce')
    df['revenue']=df['revenue'].apply(parsing.check_float)


    # x=np.log10(df['runtime'])
    # y=np.log10(df['revenue'])

    plt.figure(figsize=(8,6))
    plt.scatter(df['runtime'], df['revenue'], alpha=0.3, s=10)
    # plt.scatter(x, df['revenue'], alpha=0.3, s=10)
    plt.yscale('symlog')
    plt.title("Runtime vs Revenue")
    plt.xlabel("Runtime (minutes)")
    plt.ylabel("Revenue (USD, symlog scale)")
    plt.tight_layout()
    # plt.savefig("plots/runtime_vs_revenue.png")
    
    plt.show()



