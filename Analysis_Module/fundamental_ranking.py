import pandas as pd
import csv


tmp_df = pd.DataFrame(columns=["Country","Sector","Industry","Net_Income_Ratio","Operating_Ratio_Income",
                               "Gross_Profit_Ratio","EPS","Working_Capital","ROE",
                               "PE_Ratio","PB_Ratio","Current_Ratio","Debt_To_Equity","Debt_To_Asset",
                               "Dividend_Yield","Market_Capital"])

with open("/data/opt/users/destiny/resource/Stock_List.csv") as stocklist:
#with open("C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\Stock_List.csv") as stocklist:
    stocklist_r = csv.reader(stocklist)
    next(stocklist_r)
    
    for row in stocklist_r:


        ######################################################  
        #               Fetching from profile                #
        ######################################################
        try:
            filename = "/data/opt/users/destiny/resource/profile/"+row[0]+"_Profile.csv"
            with open(filename) as profile:
            #with open("C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Example\\Profile.csv") as profile:
                profile_r = [row for row in csv.reader(profile)]
                country = profile_r[21][1]
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
                Net_Income_Ratio = in_s_r[25][1]
                Operating_Ratio_Income = in_s_r[19][1]
                Gross_Profit_Ratio = in_s_r[7][1]
                EPS = in_s_r[26][1]
        except IOError:
            Net_Income_Ratio = "NaN"
            Operating_Ratio_Income = "NaN"
            Gross_Profit_Ratio = "NaN"
            EPS = "NaN"
        
        
        ######################################################  
        #             Fetching from key metric               #
        ######################################################
        try:
            filename = "/data/opt/users/destiny/resource/key_metric/"+row[0]+"_KeyMetric.csv"
            with open(filename) as km:
            #with open("C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Example\\KeyMetric.csv") as km:
                km_r = [row for row in csv.reader(km)]
                Working_Capital = km_r[43][1]
                ROE = km_r[56][1]
                PE_Ratio = km_r[12][1]
                PB_Ratio = km_r[16][1]
                Current_Ratio = km_r[27][1]
                Debt_To_Equity = km_r[16][1]
                Debt_To_Asset = km_r[25][1]
                Dividend_Yield = km_r[30][1]
                Market_Capital = km_r[10][1]
        except IOError:
            Working_Capital = "NaN"
            ROE = "NaN"
            PE_Ratio = "NaN"
            PB_Ratio = "NaN"
            Current_Ratio = "NaN"
            Debt_To_Equity = "NaN"
            Debt_To_Asset = "NaN"
            Dividend_Yield = "NaN"
            Market_Capital = "NaN"
        

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
    print(tmp_df)