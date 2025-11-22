import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def check_float(x):
    try:
        return float(str(x).replace(',', '').replace('$', ''))
    except:
        return np.nan
    

