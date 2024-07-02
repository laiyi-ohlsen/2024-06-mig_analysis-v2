import pandas as pd
import numpy as np
from scipy import stats

df =  pd.read_csv('data/both_unfiltered_raw.csv')

df = df.loc[df['site'] == 'del05']

print(len(df.index))
print(df['date'].unique())