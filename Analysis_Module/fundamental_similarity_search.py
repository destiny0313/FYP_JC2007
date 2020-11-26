import falconn as fal
import numpy as np
import pandas as pd
import os

x = fal.LSHIndex(fal.get_default_parameters)
filepath = os.path.abspath(os.getcwd())+"//..//Source//attribute_ranking.csv"
with open(filepath) as ranking:
    df_tmp = pd.read_csv(ranking)
    
df_tmp = df_tmp.drop(['Unnamed: 0', 'Country','Sector','Industry'], axis=1)
df = pd.DataFrame.to_numpy(df_tmp)
print(df_tmp)
    
x.setup(df)