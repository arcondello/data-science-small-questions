import pandas as pd
import numpy as np
import os
import re
import matplotlib.pyplot as plt


years = [int(re.findall('\d{4}', file)[0]) for file in os.listdir('names') if re.search('\d{4}', file)]

frames = []
for yr in years:
    df = pd.read_csv('names/yob%d.txt' % yr, names=['Name','Sex','Births'])
    df['Year']=yr
    frames.append(df)
    
names = pd.concat(frames, ignore_index=True)

# Q1: Add a column containing the number of letters in each name

names['Letter Count'] = names.apply(lambda row : len(row['Name']), axis=1)

# Q2: (bonus): Add a column that gives (average for the year - number of letters in name) for each name

names['Q2']=np.zeros(names.shape[0])
for year, group in names.groupby('Year'):      
    total_letters = group['Letter Count'].multiply(group['Births']).sum()
    total_births = group['Births'].sum()
    names.loc[names['Year']==year,'Q2']=total_letters/float(total_births)
    
names['Q2']=names['Q2']-names['Letter Count']    

print names