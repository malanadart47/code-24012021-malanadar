#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:39:54 2021

@author: malanadar
"""

import pandas as pd
import numpy as np

json_data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

df = pd.DataFrame(json_data)
refer_data = pd.DataFrame([['Underweight','18.4 and below','Malnutrition risk'],
                           ['Normal weight','18.5 - 24.9','Low risk'], 
                           ['Overweight','25 - 29.9','Enhanced risk'],
                           ['Moderately obese','30 - 34.9','Medium risk'],
                           ['Severely obese	35','35 - 39.9'	,'High risk'],
                           ['Very severely obese','40 and above','Very high risk']], columns=('BMI Category', 'BMI Range (kg/m2)', 'Health risk'))


def check(h):
    a=h.split(' ')
    if a[2]=='below':
        a[2]=a[0]
        a[0]=0
    if a[2]=='above':
        del a[2]
        #a.remove(2)
    #a.remove(1)
    del a[1]
    list_of_floats = [float(item) for item in a]
    return list_of_floats

k=[]
for j in refer_data['BMI Range (kg/m2)']:
    k.append(check(j))

    
f=[]
d=[]          
def finds(j,k):
    v=0
    for k1,j2  in enumerate(k):
        if len(j2)==1:
            if j>j2[0]:
               v=k1 
        elif j>=float(j2[0]) and j<=float(j2[1]):
            v=k1
        else:
            pass
    return v


#Solution 1:
#BMI(kg/m2) = mass(kg) / height(m)2
df['Bmi Calculated']=df['WeightKg']/(df['HeightCm']/100)**2
df['BMI Category'] = [refer_data['BMI Category'][finds(x,k)]  for x in df['Bmi Calculated'] if finds(x,k)>0]
df['Health risk']=[refer_data['Health risk'][finds(x,k)]  for x in df['Bmi Calculated'] if finds(x,k)>0]

"""
f=[]
d=[] 
for j in df['Bmi Calculated']:
    c=finds(float(j),k)
    d.append(refer_data['BMI Category'][c])
    f.append(refer_data['Health risk'][c])
df['BMI Category']=d
df['Health risk']=f
"""
    
#Solution 2:
    
sum_overweight=np.sum(df['BMI Category'] =='Overweight')
#Additional details:
idx = pd.Index(df['BMI Category'].tolist(), name ='Category') 
idx.value_counts() 
    