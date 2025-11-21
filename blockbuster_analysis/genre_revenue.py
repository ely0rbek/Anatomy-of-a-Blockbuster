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
    genres=df['genres'].apply(parse_genre)
    revenue=df['revenue'].apply(check_float)

    print(type(genres))
    print(genres[0:2])

    


plot_genre_revenue()