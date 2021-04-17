# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:33:07 2020

@author: user
"""

import FundamentalAnalysis as fa
import csv
import pandas as pd

api_key = "6e5ecde1494f8945f457010be7b7920e" # API key for accessing FA package



#with open('C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\Stock_list.csv','r') as stocklist:
#    fp = open('C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\FinancialData_ErrorLog.txt','a')
with open('//data//opt//users//destiny//real//resource//Stock_List.csv','r') as stocklist:
    fp = open('//data//opt//users//destiny//real//resource//FinancialData_ErrorLog.txt','a')
    #with open('C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\Financial_Data.csv','w') as datalist:
    #with open('//data//opt//users//destiny//real//resource//Financial_Data.csv','w') as datalist:

        #fields = ['Stock','Asset','Liability','Equity']
        #datawriter = csv.DictWriter(datalist, fields)
        #datawriter.writeheader()
        
    rstocklist = csv.reader(stocklist)
    next(rstocklist)
        
    for row in rstocklist:
            
        print("Processing "+row[0])
        income_statement_annually = fa.income_statement(row[0], api_key, period="annual")
        key_metric = fa.key_metrics(row[0], api_key, period="annual")
        balance_sheet = fa.balance_sheet_statement(row[0], api_key, period="annual")
        enterprise = fa.enterprise(row[0], api_key, period="annual")
        profile = fa.profile(row[0], api_key)
            
        if key_metric.empty:
            fp.writelines(row[0] + "has no available key metric")
        else:
            km_df = pd.DataFrame(key_metric)
            #name_km = "C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\km\\"+row[0]+"_KeyMetric.csv"
            name_km = "//data//opt//users//destiny//real//resource//key_metric//"+row[0]+"_KeyMetric.csv"
            km_df.to_csv(name_km)

            
        if income_statement_annually.empty:
            fp.writelines(row[0] + "has no available annual income statement")
        else:
            isa_df = pd.DataFrame(income_statement_annually)
            #name_isa = "C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\isa\\"+row[0]+"_IncomeStatement.csv"
            name_isa = "//data//opt//users//destiny//real//resource//income_statement_annual//"+row[0]+"_IncomeStatement.csv"
            isa_df.to_csv(name_isa)
     
            
        if balance_sheet.empty:
            fp.writelines(row[0] + "has no available balance sheet")
        else:
            bs_df = pd.DataFrame(balance_sheet)
            #name_bs = "C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\bs\\"+row[0]+"_BalanceSheet.csv"
            name_bs = "//data//opt//users//destiny//real//resource//balance_sheet//"+row[0]+"_BalanceSheet.csv"
            bs_df.to_csv(name_bs)
           
            
        if enterprise.empty:
            fp.writelines(row[0] + "has no available enterprise")
        else:
            enterprise_df = pd.DataFrame(enterprise)
            #name_e = "C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\e\\"+row[0]+"_Enterprise.csv"
            name_e = "//data//opt//users//destiny//real//resource//enterprise//"+row[0]+"_Enterprise.csv"
            enterprise_df.to_csv(name_e)
            
            
        if profile.empty:
            fp.writelines(row[0] + "has no available profile")
        else:       
            profile_df = pd.DataFrame(profile) 
            #name_p = "C:\\Users\\desti\\Documents\\GitHub\\FYP_JC2007\\Source\\p\\"+row[0]+"_Profile.csv"
            name_p = "//data//opt//users//destiny//real//resource//profile//"+row[0]+"_Profile.csv"
            profile_df.to_csv(name_p)
                
            
            #if balance_sheet.empty:
            #    print("No balance sheet available")
            #else:
            #    print(balance_sheet["2019"]["totalAssets"])
            #    print(balance_sheet["2019"]["totalLiabilities"])
            #    print(balance_sheet["2019"]["longTermDebt"])
            #    print(balance_sheet["2019"]["shortTermDebt"])
                
            
            
            #if income_statement_annually.empty:
            #    print("No income statement available")
            #else:
            #    print(income_statement_annually["2019"]["eps"])
            #    print(income_statement_annually["2019"]["netIncome"])
            #    print(income_statement_annually["2019"]["revenue"])
            #    print(income_statement_annually["2019"]["grossProfit"])
            
            #if profile.empty:
            #    print("No profile available")
            #else:
            #    print(profile[0]["mktCap"])
            #    print(profile[0]["sector"])
            #    print(profile[0]["industry"])
            #    print(profile[0]["country"])
            #    print(profile[0]["city"])
            #    print(profile[0]["state"])
                
            
            #if income_statement_annually.empty:
            #    print("No Data Available")
            #else:
            #    print(income_statement_annually['2019']['currentRatio'])
