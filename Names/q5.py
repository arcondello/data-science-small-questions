

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


# Q1: Sort by number of births

names.sort('Births', inplace=True)

# Q2: Find the value of the 173rd row, 2nd column
print '173rd row, 2nd column:', names.iloc[173,2]

# Q3: What is the year for the 1198th row?
print 'Year of the 1198th row:', names.iloc[1198]['Year']

# Q4: Pivot or Unstack so that the frame is organized by name, with a column for each year giving the number of births
births_by_year = names.set_index(['Name','Sex','Year']).unstack()
#print births_by_year