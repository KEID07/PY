# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:35:54 2018

@author: Keid07
"""

#obj_data is a dataset containing id, CR, CLICK and BIDDING.

import pandas as pd
from sklearn.linear_model import LinearRegression

obj_data = pd.read_excel(<directory>,sheet_name=<'Sheet1'>)

obj_data['id']=obj_data['id'].astype(str)
obj_data_clean = obj_data[obj_data['CLICK']>=3000]
obj_data_clean = obj_data[obj_data['CR']<1]

unique_data = obj_data_clean['appid&country'].drop_duplicates(keep='first')
result = []
intercept = []
feature_cols = ['CLICK','BIDDING']
linreg = LinearRegression()
for x in unique_data:
    data = obj_data_clean[obj_data_clean['appid&country'] == x]
    xtrain = data[['CLICK','BIDDING']]
    ytrain = data['CR']
    model=linreg.fit(xtrain,ytrain)
    z = dict(zip(feature_cols,linreg.coef_))
    result.append(z)
    intercept.append(linreg.intercept_)
    
result_table = pd.DataFrame(data = result,index = unique_data)
intercept_table = pd.DataFrame(data = intercept,index = unique_data,columns = ['A_'])
final_result = pd.merge(intercept_table,result_table,on='appid&country')

final_result.to_csv(<directory>)