import pandas as pd
import numpy as np
import os
import re
import matplotlib.pyplot as plt


years = [int(re.findall('\d{4}', file)[0]) for file in os.listdir('names') if re.search('\d{4}', file)]



# frames = []
# for yr in years:
#     df = pd.read_csv('names/yob%d.txt' % yr, names=['Name','Sex','Births'])
#     df['Year']=yr
#     frames.append(df)


f = lambda yr : pd.read_csv('names/yob%d.txt' % yr, names=['Name','Sex','Births'])
names = pd.concat(map(f, years), ignore_index=True)

# Q1: Create a new column in the dataset entitled 'F' with value 1 as an int if the name is female, or 0 if the name if male
# Q2: Create a 'M' column the the values inverted, please do this a different way
# Q3 (bonus): Create a column '%' that indicated the percentage each name represents for its year.

###################################################################
# Q1
if False:
    names['F'] = names.apply(lambda row : int(row['Sex']=='F'), axis=1)
    print names

###################################################################    
# Q2
if False:
    names['M']=np.zeros(names.shape[0])
    names.loc[names['Sex']=='M', 'M'] = 1
    print names
    
###################################################################    
# Q3
if False:
    names['%']=np.zeros(names.shape[0])
    for year, group in names.groupby('Year'):      
        total_births = group['Births'].sum()
        names.loc[names['Year']==year, '%'] = names.loc[names['Year']==year, 'Births']/float(total_births)

    print names