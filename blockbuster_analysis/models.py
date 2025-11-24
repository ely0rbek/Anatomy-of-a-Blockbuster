import numpy as np
import pandas as pd
import ast

class csv_paths:
    def __init__(self):
        self.csv_movies_path="D:\python\Anatomy_of_Blockbuster\datasets\\movies_metadata.csv"
        self.csv_ratings_path="D:\python\Anatomy_of_Blockbuster\datasets\\ratings_small.csv"
        self.csv_links_path="D:\python\Anatomy_of_Blockbuster\datasets\\links_small.csv"

    def get_movies_path(self):
        return self.csv_movies_path
    
    def get_ratings_path(self):
        return self.csv_ratings_path
    
class Parsing:
    def parse_float(self,x):
        try:
            return float(str(x).replace(',', '').replace('$', ''))
        except:
            return np.nan

    def parse_genres(self,x):
        if pd.isna(x): return []
        try:
            data = ast.literal_eval(x)
            if isinstance(data, list):
                return [d.get('name', '') for d in data if isinstance(d, dict)]
        except:
            return []
        return []
    




# def parse_genres(x):
#     if pd.isna(x): return []
#     try:
#         data = ast.literal_eval(x)
#         if isinstance(data, list):
#             return [d.get('name', '') for d in data if isinstance(d, dict)]
#     except Exception:
#         return []
#     return []

# def check_float(x):
#     try:
#         return float(str(x).replace(',', '').replace('$', ''))
#     except:
#         return np.nan