# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:14:43 2025

@author: RylaElli

I will extract price data from Sproule.

"""
#%% Import Packages
import requests
import pandas as pd

#%% Run Parameters

url = "https://sproule.com/wp-content/uploads/2025/01/2024-12-Escalated-6.xlsx"

#%% Functions

def get_df(url):
    response = requests.get(url)
    code = response.status_code
    if code == 200:    
        df = pd.read_excel(url, sheet_name='North American Oil', header=7, usecols='B,F:L')
        return df
    else:
        print('Error: Could not retrieve url')
        print('Status Code: ', str(code))
        return None

def clean_df(df):
    df.dropna(inplace=True)
    df['Year'] = pd.to_numeric(df['Year'].str[0:4])
    df = df[df['Year'] < 2024]
    return df
    

#%% Run
if __name__ == '__main__':
    df = get_df(url)
    df_clean = clean_df(df)