import pandas as pd
import numpy as np

df = pd.read_csv("D:\python\BlockbusterDB\\movies_metadata.csv",low_memory=False)

revenues= list(map(float,df["revenue"]))

released_dates=pd.to_datetime(df['release_date'], errors='coerce')

print(released_dates[:10])

print(revenues[:10])

