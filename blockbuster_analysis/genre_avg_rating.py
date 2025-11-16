import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast, os

def parse_genres(x):
    if pd.isna(x): return []
    try:
        data = ast.literal_eval(x)
        if isinstance(data, list):
            return [d.get('name', '') for d in data if isinstance(d, dict)]
    except:
        return []
    return []

