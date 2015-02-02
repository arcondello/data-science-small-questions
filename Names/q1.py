# Day 1 is just taken from Python for Data Analysis chp 1. If you have trouble importing, you can follow the instructions there.
# Download the US Census Data on baby names, 1880-present, from here:
# http://www.ssa.gov/oact/babynames/limits.html
# Q1: How many babies were born in 1914?
# Q2: How has the ratio of males/females changed over time? (optional--plot)
# Q3: How popular was your name over time? (optional-- plot)
# Q4: How has the number of letters in baby names changed over time? (optional-- plot)



import pandas as pd
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

###################################################################################
# Q1

if False :
    test = names['Year']==1914
    
    print test
    
    df = names[test]
    
    solution = df['Births'].sum()
    #print 'Question 1:', df['Births'].sum(), 'Babies Born'

###################################################################################
# Q2

if False:
    year_list = []
    ratio_list = []
    
    grouped = names.groupby('Year')
    
    for year, group in grouped:
        #print year, group
        
        year_list.append(year)
        gen_dict = {}
        for gender, gp in group.groupby('Sex'):
            gen_dict[gender] = float(gp['Births'].sum())
        ratio_list.append(gen_dict['M']/gen_dict['F'])
    solution = zip(year_list, ratio_list)
    plt.plot(solution)
    plt.show()
    
###################################################################################
# Q3
if False:
    my_name = 'Alexander'
    year_list = []
    count_list = []
    for year, group in names[names['Name']==my_name].groupby('Year'):
        year_list.append(year)
        count_list.append(group['Births'].sum())
        
    for yr in years :
        if yr not in year_list :
            year_list.append(yr)
            count_list.append(0)
            
    plt.plot(year_list,count_list)
    plt.show()
    
###################################################################################
# Q4
if True:
    year_list = []
    letter_list = []
    for year, group in names.groupby('Year'):
        year_list.append(year)
        letter_list.append((group.apply(lambda row : len(row['Name']), axis=1)*group['Births']).sum()/float(group['Births'].sum()))
        
    plt.plot(year_list,letter_list)
    plt.show()
        
        







