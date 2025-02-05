# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:57:07 2025

@author: RylaElli
"""

import numpy as np
import pandas as pd
from helpers import acf
from statsmodels.tsa.stattools import acf as smacf

df = pd.read_csv('df.csv')
wcs = np.array(df['WCS'])
year = np.arange(0, wcs.size)

acf = acf(wcs, 5)
acf_check = smacf(wcs, 5)

def auto_regress():
    pass