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

# Q1: Sort by number of births per name
# Q2: On the original frame, add a column with the first letter of each name
# Q3: Which letter has appeared the most? The least?



if False: # Q1
    names_year = names.set_index(['Name','Sex','Year']).unstack()

    names_year['Total']=names_year.sum(axis=1)

    print names_year.sort('Total')
    
if True: # Q2
    names['First Letter']=names.apply(lambda row : row['Name'][0], axis=1)
    print names
    
    if True: # Q3
        letter_dict = {}
        def update_letter_dict(row):
            l = row['First Letter']
            if l in letter_dict:
                letter_dict[l]=letter_dict[l]+row['Births']
            else:
                letter_dict[l]=row['Births']
        names.apply(update_letter_dict, axis=1)
        
        print letter_dict