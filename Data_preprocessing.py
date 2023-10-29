import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns',40)

df=pd.read_csv('data.csv')
#dropping the unnamed column
df.drop('Unnamed: 0',axis=1,inplace=True)

#issues to resolve (Issue 3)

#sum up all the plotareas for each household
cols_fplot=df.columns[df.columns.str.contains('fplotarea')]
df['total_plotarea']=df[cols_fplot].sum(axis=1)

#drop fplotarea1, fplotarea2 and fplotarea3
df.drop(columns=cols_fplot, inplace=True)

#reduce fsystem to one column which returns the most common farmsystem used by each household,
#for those with more than one common farm system, return the values that are common
cols_fsystem=df.columns[df.columns.str.contains('fsystem')]
fsystem_mode=df[cols_fsystem].mode(axis=1)[0]
df['frequent_fsystem']=fsystem_mode

#drop cols with fsystem
df.drop(columns=cols_fsystem,inplace=True)


#reduce the tenure to one column which returns the most common tenure system used by each household, 
#for those with more than one common tenure system, return the values that are common
cols_tenure=df.columns[df.columns.str.contains('tenure')]
tenure_mode=df[cols_tenure].mode(axis=1)[0]
df['frequent_tenure']=tenure_mode

#drop cols with tenure
df.drop(columns=cols_tenure,inplace=True)

#reduce yearuse1 to one colum which returns the average number of years of use of each farmland
cols_year=df.columns[df.columns.str.contains('yearsuse')]
avg_yearsuse=df[cols_year].mean(axis=1)
df['avg_yearsuse']=avg_yearsuse

#drop cols with yearsuse
df.drop(columns=cols_year,inplace=True)

#reduce rentplot to one column which returns the average years each land is rented for each household
cols_rent=df.columns[df.columns.str.contains('rentplot')]
avg_rentplot=df[cols_rent].mean(axis=1)
df['avg_rentplot']=avg_rentplot

#drop cols with rentplot
df.drop(columns=cols_rent,inplace=True)

#drop season3 (since there are only 2 seasons in Africa)
df.drop(columns=['season3s','season3e','seas3nam'],inplace=True)

#drop all activites that have to do with season3
#dropping the values in the first column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hm3')],inplace=True)

#dropping the values in the second column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hmd3')],inplace=True)

#dropping the values in the third column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hhf3')],inplace=True)

#dropping the values in the fourth column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hfd3')],inplace=True)

#dropping the values in the fifth column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hhc3')],inplace=True)

#dropping the values in the sixth column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hcd3')],inplace=True)

#dropping the values in the seven column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hrm3')],inplace=True)

#dropping the values in the eight column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('rmd3')],inplace=True)

#dropping the values in the ninth column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hrf3')],inplace=True)

#dropping the values in the tenth column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hrfd3')],inplace=True)

#dropping the values in the eleventh column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('hrc3')],inplace=True)

#dropping the values in the twelfth column in the survey table
df.drop(columns=df.columns[df.columns.str.contains('rcd3')],inplace=True)

#reduce the household columns to calculate:

#number of household labor

#average number of days for household labor

#reduce hired labor columns to calculate:

#number of hired labor

#average number of days for hired labor

#columns for all household laborers (male, female, children)
cols_labor=(df.columns[df.columns.str.contains('hhf1')].
      append(df.columns[df.columns.str.contains('hhm1')]).
      append(df.columns[df.columns.str.contains('hhc1')]))

household_labor=df[cols_labor].count(axis=1)
df['season1_count_household_labor']=household_labor

#drop the columns
df.drop(columns=cols_labor, inplace=True)

#columns for household number of days
cols_days=(df.columns[df.columns.str.contains('hhmd1')].
      append(df.columns[df.columns.str.contains('hhfd1')]).
      append(df.columns[df.columns.str.contains('hhcd1')]))

household_labor=df[cols_days].mean(axis=1)
df['season1_avg_household_days']=household_labor

#drop the columns
df.drop(columns=cols_days, inplace=True)

#columns for all hired laborers (male, female, children)
cols_hire=(df.columns[df.columns.str.contains('hrf1')].
      append(df.columns[df.columns.str.contains('hrm1')]).
      append(df.columns[df.columns.str.contains('hrc1')]))

hired_labor=df[cols_hire].sum(axis=1)
df['season1_sum_hired_labor']=hired_labor

#drop the columns
df.drop(columns=cols_hire, inplace=True)

#columns for all hired number of days
cols_hiredays=(df.columns[df.columns.str.contains('hrfd1')].
      append(df.columns[df.columns.str.contains('hrmd1')]).
      append(df.columns[df.columns.str.contains('hrcd1')]))

hired_labor=df[cols_hiredays].mean(axis=1)
df['season1_avg_hired_labor']=hired_labor

#drop the columns
df.drop(columns=cols_hiredays, inplace=True)

##Do similar for SEASON2
#columns for all household laborers (male, female, children)
cols_house=(df.columns[df.columns.str.contains('hhf2')].
      append(df.columns[df.columns.str.contains('hhm2')]).
      append(df.columns[df.columns.str.contains('hhc2')]))

household_labor=df[cols_house].sum(axis=1)
df['season2_count_household_labor']=household_labor

#drop the columns
df.drop(columns=cols_house, inplace=True)

#columns for household number of days
cols_days=(df.columns[df.columns.str.contains('hhmd2')].
      append(df.columns[df.columns.str.contains('hhfd2')]).
      append(df.columns[df.columns.str.contains('hhcd2')]))

household_labor=df[cols_days].mean(axis=1)
df['season2_avg_household_days']=household_labor

#drop the columns
df.drop(columns=cols_days, inplace=True)

#columns for all hired laborers (male, female, children)
cols=(df.columns[df.columns.str.contains('hrf2')].
      append(df.columns[df.columns.str.contains('hrm2')]).
      append(df.columns[df.columns.str.contains('hrc2')]))

hired_labor=df[cols].sum(axis=1)
df['season2_count_hired_labor']=hired_labor

#drop the columns
df.drop(columns=cols, inplace=True)

#columns for all hired number of days
cols=(df.columns[df.columns.str.contains('hrfd2')].
      append(df.columns[df.columns.str.contains('hrmd2')]).
      append(df.columns[df.columns.str.contains('hrcd2')]))

hired_labor=df[cols].mean(axis=1)
df['season2_avg_hired_labor']=hired_labor

#drop the columns
df.drop(columns=cols, inplace=True)

#do the same for livestock, calculate the sum of household labor for livestock in each household
df['livestock_household_labor']=df['livshhm']+df['livshhf']+df['livshhc']

#drop the columns
df.drop(columns=['livshhm','livshhf','livshhc'],inplace=True)

#do the same for number of days
df['livestock_avg_household_days']=df[['livshhmd','livshhfd','livshhcd']].mean(axis=1)

#drop the columns
df.drop(columns=['livshhmd','livshhfd','livshhcd'],inplace=True)

#do same for hired labor
df['livestock_hired_labor']=df['livshrm']+df['livshrf']+df['livshrc']
#drop the columns
df.drop(columns=['livshrm','livshrf','livshrc'],inplace=True)

df['livestock_avg_hired_days']=df[['livshrmd','livshrfd','livshrcd']].mean(axis=1)
#drop the columns
df.drop(columns=['livshrmd','livshrfd','livshrcd'],inplace=True)

#do the same thing for average wage
df['avg_household_wage']=df[['wagehhm','wagehhf','wagehhc']].mean(axis=1)

#drop the columns
df.drop(columns=['wagehhm','wagehhf','wagehhc'],inplace=True)

#do the same thing for average wage
df['avg_hired_wage']=df[['wagehrm','wagehrf','wagehrc']].mean(axis=1)

#drop the columns
df.drop(columns=['wagehrm','wagehrf','wagehrc'],inplace=True)

#do the same for inkind payment
df['total_household_kind_payment']=df[['inkindhhm','inkindhhf','inkindhhc']].sum(axis=1)

#drop the columns
df.drop(columns=['inkindhhm','inkindhhf','inkindhhc'],inplace=True)

df['total_hired_kind_payment']=df[['inkindhrm','inkindhrf','inkindhrc']].sum(axis=1)

#drop the columns
df.drop(columns=['inkindhrm','inkindhrf','inkindhrc'],inplace=True)