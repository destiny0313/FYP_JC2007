import pandas as pd
import csv
import numpy as np


tmp_df = pd.DataFrame(columns=["Country","Sector","Industry","Net_Income_Ratio","Operating_Ratio_Income",
                               "Gross_Profit_Ratio","EPS","Working_Capital","ROE",
                               "PE_Ratio","PB_Ratio","Current_Ratio","Debt_To_Equity","Debt_To_Asset",
                               "Dividend_Yield","Market_Capital"])

with open("/data/opt/users/destiny/resource/Stock_List.csv") as stocklist:
#with open("C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\Stock_List.csv") as stocklist:
    stocklist_r = csv.reader(stocklist)
    next(stocklist_r)
    
    for row in stocklist_r:
        print(row[0])


        ######################################################  
        #               Fetching from profile                #
        ######################################################
        try:
            filename = "/data/opt/users/destiny/resource/profile/"+row[0]+"_Profile.csv"
            with open(filename) as profile:
            #with open("C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Example\\Profile.csv") as profile:
                profile_r = {}
                for row in csv.reader(profile):
                    profile_r[row[0]] = row
                    
                if profile_r.get("country")[1] =="":
                    country = "NaN"
                else:
                    country = profile_r.get("country")[1]
                    
                if profile_r.get("sector")[1]=="":
                    sector="NaN"
                else:
                    sector = profile_r.get("sector")[1]
                    
                if profile_r.get("industry")[1] == "":
                    industry = "NaN"
                else:
                    industry = profile_r.get("industry")[1]
        except IOError:
            country = "NaN"
            industry = "NaN"
            sector = "NaN"


        ######################################################  
        #          Fetching from income statement            #
        ######################################################
        try:
            filename = "/data/opt/users/destiny/resource/income_statement_annual/"+row[0]+"_IncomeStatement.csv"
            with open(filename) as in_s:
                in_s_r = {}
                for row in csv.reader(in_s):
                    in_s_r[row[0]] = row
                    
                if in_s_r.get("netIncomeRatio")[1] == "":
                    Net_Income_Ratio = np.NaN
                else:
                    Net_Income_Ratio = float(in_s_r.get("netIncomeRatio")[1])
                
                if in_s_r.get("operatingIncomeRatio")[1] == "":
                    Operating_Ratio_Income = np.NaN
                else:
                    Operating_Ratio_Income = float(in_s_r.get("operatingIncomeRatio")[1])
                
                if in_s_r.get("grossProfitRatio")[1] =="":
                    Gross_Profit_Ratio = np.NaN
                else:
                    Gross_Profit_Ratio = float(in_s_r.get("grossProfitRatio")[1])
                
                if in_s_r.get("eps")[1] == "":
                    EPS = np.NaN
                else:
                    EPS = float(in_s_r.get("eps")[1])
        except IOError:
            Net_Income_Ratio = np.NaN
            Operating_Ratio_Income = np.NaN
            Gross_Profit_Ratio = np.NaN
            EPS = np.NaN
        
        
        ######################################################  
        #             Fetching from key metric               #
        ######################################################
        try:
            filename = "/data/opt/users/destiny/resource/key_metric/"+row[0]+"_KeyMetric.csv"
            with open(filename) as km:
            #with open("C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Example\\KeyMetric.csv") as km:
                km_r = {}
                for row in csv.reader(km):
                    km_r[row[0]] = row
                    
                if km_r.get("workingCapital")[1] == "":
                    Working_Capital = np.NaN
                else:
                    Working_Capital = float(km_r.get("workingCapital")[1])
                
                if km_r.get("roe")[1] == "":
                    ROE = np.NaN
                else:
                    ROE = float(km_r.get("roe")[1])
                
                if km_r.get("peRatio")[1] == "":
                    PE_Ratio = np.NaN
                else:
                    PE_Ratio = float(km_r.get("peRatio")[1])
                
                if km_r.get("pbRatio")[1] == "":
                    PB_Ratio = np.NaN
                else:
                    PB_Ratio = float(km_r.get("pbRatio")[1])
                
                if km_r.get("currentRatio")[1] == "":
                    Current_Ratio = np.NaN
                else:
                    Current_Ratio = float(km_r.get("currentRatio")[1])
                
                if km_r.get("debtToEquity")[1] == "":
                    Debt_To_Equity = np.NaN
                else:
                    Debt_To_Equity = float(km_r.get("debtToEquity")[1])
                
                if km_r.get("debtToAssets")[1] == "":
                    Debt_To_Asset = np.NaN
                else:
                    Debt_To_Asset = float(km_r.get("debtToAssets")[1])
                    
                if km_r.get("dividendYield")[1] =="":
                    Dividend_Yield = np.NaN
                else:
                    Dividend_Yield = float(km_r.get("dividendYield")[1])
                    
                if km_r.get("marketCap")[1] == "":
                    Market_Capital = np.NaN
                else:
                    Market_Capital = float(km_r.get("marketCap")[1])
        except IOError:
            Working_Capital = np.NaN
            ROE = np.NaN
            PE_Ratio = np.NaN
            PB_Ratio = np.NaN
            Current_Ratio = np.NaN
            Debt_To_Equity = np.NaN
            Debt_To_Asset = np.NaN
            Dividend_Yield = np.NaN
            Market_Capital = np.NaN
        

    ######################################################  
    #              Put data into dataframe               #
    ######################################################
        stockname = row[0]
        stockname = pd.DataFrame({"Country":country,"Sector":sector,"Industry":industry,
                                  "Net_Income_Ratio":Net_Income_Ratio,"Operating_Ratio_Income":Operating_Ratio_Income,
                                  "Gross_Profit_Ratio":Gross_Profit_Ratio,"EPS":EPS,"Working_Capital":Working_Capital,
                                  "ROE":ROE,"PE_Ratio":PE_Ratio,"PB_Ratio":PB_Ratio,"Current_Ratio":Current_Ratio,
                                  "Debt_To_Equity":Debt_To_Equity,"Debt_To_Asset":Debt_To_Asset,
                                  "Dividend_Yield":Dividend_Yield,"Market_Capital":Market_Capital}, index=[stockname])

        tmp_df = tmp_df.append(stockname)
    
    df_a = tmp_df.sort_values(Working_Capital, na_position="last", ascending=True)
    list_a = list(df_a.index.values)
    print(list_a)