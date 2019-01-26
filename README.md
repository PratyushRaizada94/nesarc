# nesarc

the U.S. National Epidemiological Survey on Alcohol and Related Conditions (NESARC)  dataset for my assignment. The dataset is based on cross-sectional study and covers a lot of values regarding substance abuse by 40093 US residents, the data set is vast and covers a lot of questions that can help derive relevant information. 

For my analysis regarding remission of tobacco I’ve chosen SECTION 3A: TOBACCO USE AND DEPENDENCE

Hypothesis: Nicotine remission is independent of age

Age group is not a factor contributing to a life long nicotine addiction. There should be very small difference in percentage of people quitting smoking across different age groups should be . Because nicotine dependance can be controlled and limited at any age group as the withdrawal time is a week.

Columns associated with my assignment

1. S3AQ10D: Age at onset of nicotine dependence

2. S3AQ10I:  Age at full remission of nicotine dependence

I’ve compared the percentages of people who have attained full remission from nicotine dependance which they developed in their teenage and young adulthood.

Code:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
“”“
Created on Mon Oct 22 23:58:58 2018

@author: pratyushraizada
”“”

import numpy
import pandas

data = pandas.read_csv(‘nesarc_pds.csv’,low_memory=False)

#TIP: It’s a good practice to convert all column names to upper case before precessing
data.columns = map(str.upper,data.columns)
#Setting max number of rows to 100
pandas.set_option('display.max_rows’,110)

#[DATA MUNGING]
#Replacing blank values with -1 to have all data in numeric form
data['S3AQ10D’].replace(“ ”,-1,inplace=True)
data['S3AQ10D’] = pandas.to_numeric(data['S3AQ10D’])
data['S3AQ10I’].replace(“ ”,-1,inplace=True)
data['S3AQ10I’] = pandas.to_numeric(data['S3AQ10I’])

“’
The below satements are used to find the number of people who became nicotine
depenent in their teenage, this follows the number of people who have taken 
remission from nicotine dependence
”’

print(“COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN TEENAGE”)
s1 = data[(data['S3AQ10D’]!=-1) & (data['S3AQ10D’]<20)]
c1 = sum(s1[“S3AQ10D”].value_counts(sort=False))
print(c1)

print(“COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN TEENAGE AND ATTAINED FULL REMISSION LATER”)
s2 = data[(data['S3AQ10D’]!=-1) & (data['S3AQ10D’]<20) & (data['S3AQ10I’]!=-1) & (data['S3AQ10I’]!=99)]
c2 = sum(s2[“S3AQ10I”].value_counts(sort=False))
print(c2)

print(“PERCENTAGE TEENAGE NICOTINE DEPENDENTS SUCCESSFULLY REMISSIONED”)
p1 = (c2*100)/c1
print(p1)

“’
The below satements are used to find the number of people who became nicotine
depenent in their young adults, this follows the number of people who have taken 
remission from nicotine dependence
”’

print(“COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN YOUNG ADULTHOOD”)
s3 = data[(data['S3AQ10D’]!=-1) & (data['S3AQ10D’]>=20) & (data['S3AQ10D’]<30)]
c3= sum(s3[“S3AQ10D”].value_counts(sort=False))
print(c3)

print(“COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN YOUNG ADULTHOOD AND ATTAINED FULL REMISSION LATER”)
s4 = data[(data['S3AQ10D’]!=-1) & (data['S3AQ10D’]>=20) & (data['S3AQ10D’]<30) & (data['S3AQ10I’]!=-1) & (data['S3AQ10I’]!=99)]
c4 = sum(s4[“S3AQ10I”].value_counts(sort=False))
print(c4)

print(“PERCENTAGE YOUNG-ADULT NICOTINE DEPENDENTS SUCCESSFULLY REMISSIONED”)
p2 = (c4*100)/c3
print(p2)

Output:

COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN TEENAGE
1364
COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN TEENAGE AND ATTAINED FULL REMISSION LATER
346
PERCENTAGE TEENAGE NICOTINE DEPENDENTS SUCCESSFULLY REMISSIONED
25.366568914956012
COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN YOUNG ADULTHOOD
2126
COUNT OF PEOPLE HAVING DEVELOPED NICOTINE DEPENDENCE IN YOUNG ADULTHOOD AND ATTAINED FULL REMISSION LATER
533
PERCENTAGE YOUNG-ADULT NICOTINE DEPENDENTS SUCCESSFULLY REMISSIONED
25.070555032925682

Result:

With a mere difference of 0.29 percentage points we see the values to be almost identical and hence conclude that nicotine remission is independent of the age of nicotine dependence. Also, 1 out 4 people in teenage and young adulthood can quit nicotine addiction.
