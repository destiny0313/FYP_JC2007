from lshashpy3 import LSHash
import pandas as pd
import os

filepath = os.path.abspath(os.getcwd())+"//..//Source//attribute_ranking.csv"

lsh = LSHash(6,13)

with open(filepath) as ranking:
    df = pd.read_csv(ranking)
    df.fillna(0, inplace = True)
    
    print(df)
    i = 0
    for index,row in df.iterrows():
        lsh.index([row["Net_Income_Ratio"], row["Operating_Income_Ratio"], row["Gross_Profit_Ratio"],
                   row["EPS"], row["Working_Capital"], row["ROE"], row["PE_Ratio"], row["PB_Ratio"],
                   row["Current_Ratio"], row["Debt_To_Equity"], row["Debt_To_Asset"], row["Dividend_Yield"],
                   row["Market_Capital"]], extra_data = row["Unnamed: 0"])
    query = "TSLA"
    target = []
    for index,row in df.iterrows():
        if row["Unnamed: 0"] == query:
            target.extend([row["Net_Income_Ratio"], row["Operating_Income_Ratio"], row["Gross_Profit_Ratio"],
                   row["EPS"], row["Working_Capital"], row["ROE"], row["PE_Ratio"], row["PB_Ratio"],
                   row["Current_Ratio"], row["Debt_To_Equity"], row["Debt_To_Asset"], row["Dividend_Yield"],
                   row["Market_Capital"]])
    top_n = 10
    result = lsh.query(target, num_results=top_n, distance_func="euclidean")
    for((vec,extra_data),distance) in result:
        print(extra_data)