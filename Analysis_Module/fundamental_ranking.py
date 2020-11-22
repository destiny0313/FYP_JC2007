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
                profile_r = [row for row in csv.reader(profile)]
                if profile_r[21][1]=="":
                    country = "NaN"
                else:
                    country = profile_r[21][1]
                if profile_r[20][1]=="":
                    sector="NaN"
                else:
                    sector = profile_r[20][1]
                industry = profile_r[16][1]
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
                in_s_r = [row for row in csv.reader(in_s)]
                Net_Income_Ratio = float(in_s_r[25][1])
                Operating_Ratio_Income = float(in_s_r[19][1])
                Gross_Profit_Ratio = float(in_s_r[7][1])
                EPS = float(in_s_r[26][1])
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
                km_r = [row for row in csv.reader(km)]
                Working_Capital = float(km_r[43][1])
                ROE = float(km_r[56][1])
                PE_Ratio = float(km_r[12][1])
                PB_Ratio = float(km_r[16][1])
                Current_Ratio = float(km_r[27][1])
                Debt_To_Equity = float(km_r[16][1])
                Debt_To_Asset = float(km_r[25][1])
                if km_r[30][1]=="":
                    Dividend_Yield = np.NaN
                else:
                    Dividend_Yield = float(km_r[30][1])
                Market_Capital = float(km_r[10][1])
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
                                  "Gross_Peofit_Ratio":Gross_Profit_Ratio,"EPS":EPS,"Working_Capital":Working_Capital,
                                  "ROE":ROE,"PE_Ratio":PE_Ratio,"PB_Ratio":PB_Ratio,"Current_Ratio":Current_Ratio,
                                  "Debt_To_Equity":Debt_To_Equity,"Debt_To_Asset":Debt_To_Asset,
                                  "Dividend_Yield":Dividend_Yield,"Market_Capital":Market_Capital}, index=[stockname])

        tmp_df = tmp_df.append(stockname)
    
    df_a = tmp_df.sort_values(Working_Capital, na_position="last", ascending=True)
    list_a = list(df_a.index.values)
    print(list_a)