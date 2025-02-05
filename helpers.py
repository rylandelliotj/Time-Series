# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:07:01 2025

@author: RylaElli
"""
import numpy as np

test = np.array([1, 4, 3, 4, 5, 6, 7, 8, 9, 10])

def pearson(x,y):
    num = np.sum((x - np.mean(x)) * (y - np.mean(y))) # Covariance
    demx = np.sum((x - np.mean(x))**2) # Standard Deviation of x
    demy = np.sum((y - np.mean(y))**2) # Standard Deviation of y
    dem = np.sqrt(demx*demy)
    r = num / dem
    return r

def acf(x, lags):
    
    n = len(x)
    dem = np.sum((x - np.mean(x))**2)
    
    acf_values = []
    for k in range(lags + 1):
        num = np.sum((x[:n-k] - np.mean(x)) * (x[k:] - np.mean(x)))
        acf_k = num / dem
        acf_values.append(acf_k)
    
    return acf_values 

def pacf():
    pass