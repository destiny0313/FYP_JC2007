import os
import pandas as pd

filepath_ranking = os.path.abspath(os.getcwd())+"\\..\\Source\\attribute_ranking.csv"
df_ranking = pd.read_csv(filepath_ranking, index_col=(False))

rank_cal = {}
hii = []

for name, content in df_ranking.iterrows():
    rank_cal[content['Unnamed: 0']] = content['Dividend_Yield_Ranking']*2
    
for i in range(10):    
    hi = min(rank_cal.keys(), key=(lambda k: rank_cal[k]))
    hii.append(hi)
    rank_cal.pop(hi)
     
print(hii)