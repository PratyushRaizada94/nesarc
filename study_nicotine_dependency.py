#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 23:58:58 2018

@author: pratyushraizada
"""

import numpy
import pandas

data = pandas.read_csv('nesarc_pds.csv',low_memory=False)

#TIP: It's a good practice to convert all column names to upper case before precessing
data.columns = map(str.upper,data.columns)
#Setting max number of rows to 100
pandas.set_option('display.max_rows',110)

#[DATA MUNGING]
#Replacing blank values with -1 to have all data in numeric form
data['S3AQ10D'].replace(" ",-1,inplace=True)
data['S3AQ10D'] = pandas.to_numeric(data['S3AQ10D'])
data['S3AQ10I'].replace(" ",-1,inplace=True)
data['S3AQ10I'] = pandas.to_numeric(data['S3AQ10I'])


'''
The below satements are used to find the number of people who became nicotine
depenent in their teenage, this follows the number of people who have taken 
remission from nicotine dependence
'''

print("COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN TEENAGE")
s1 = data[(data['S3AQ10D']!=-1) & (data['S3AQ10D']<20)]
c1 = sum(s1["S3AQ10D"].value_counts(sort=False))
print(c1)

print("COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN TEENAGE AND ATTAINED FULL REMISSION LATER")
s2 = data[(data['S3AQ10D']!=-1) & (data['S3AQ10D']<20) & (data['S3AQ10I']!=-1) & (data['S3AQ10I']!=99)]
c2 = sum(s2["S3AQ10I"].value_counts(sort=False))
print(c2)

print("PERCENTAGE TEENAGE NICOTINE DEPENDENTS SUCCESSFULLY REMISSIONED")
p1 = (c2*100)/c1
print(p1)

'''
The below satements are used to find the number of people who became nicotine
depenent in their young adults, this follows the number of people who have taken 
remission from nicotine dependence
'''

print("COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN YOUNG ADULTHOOD")
s3 = data[(data['S3AQ10D']!=-1) & (data['S3AQ10D']>=20) & (data['S3AQ10D']<30)]
c3= sum(s3["S3AQ10D"].value_counts(sort=False))
print(c3)

print("COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN YOUNG ADULTHOOD AND ATTAINED FULL REMISSION LATER")
s4 = data[(data['S3AQ10D']!=-1) & (data['S3AQ10D']>=20) & (data['S3AQ10D']<30) & (data['S3AQ10I']!=-1) & (data['S3AQ10I']!=99)]
c4 = sum(s4["S3AQ10I"].value_counts(sort=False))
print(c4)

print("PERCENTAGE YOUNG-ADULT NICOTINE DEPENDENTS SUCCESSFULLY REMISSIONED")
p2 = (c4*100)/c3
print(p2)

#Generating the histogram for people developing nicotine addiction in various age groups
bin_edges = [0,10,20,30,40,50,60,70,80,90,100]
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
s5 = data[(data['S3AQ10D']!=-1)]
_ = plt.hist(s5['S3AQ10D'],bins=bin_edges)
_ = plt.xlabel('age groups')
_ = plt.ylabel('number of people becoming nicotine dependent')
plt.show()
#Generating the histogram for people developing nicotine addiction in various age groups
s6 = data[(data['S3AQ10I']!=-1) & (data['S3AQ10I']!=99)]
_ = plt.hist(s6['S3AQ10I'],bins=bin_edges)
_ = plt.xlabel('age groups')
_ = plt.ylabel('number of people becoming nicotine independent')
plt.show()