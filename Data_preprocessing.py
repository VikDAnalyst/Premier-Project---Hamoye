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

# Section 4b resolved by Victor Ademola 
# Create column for total number of livestocks owned
df["total_livestocks_owned"]=df[["lvs1num","lvs2num","lvs3num","lvs4num","lvs5num","lvs6num",
    "lvs7num","lvs8num","lvs9num","lvs10num","lvs11num","lvs12num"]].sum(axis=1)

#drop the number of each type of livestocks owned
df.drop(columns=["lvs1num","lvs2num","lvs3num","lvs4num","lvs5num","lvs6num",
    "lvs7num","lvs8num","lvs9num","lvs10num","lvs11num","lvs12num"], inplace=True)

# Create column for total nummber of livestocks born over the last 12 months
df["total_livestocks_born"]=df[["lvs1born","lvs2born","lvs3born","lvs4born","lvs5born","lvs6born",
    "lvs7born","lvs8born","lvs9born","lvs10born","lvs11born","lvs12born"]].sum(axis=1)

# drop the number of each type of livestocks born
df.drop(columns=["lvs1born","lvs2born","lvs3born","lvs4born","lvs5born","lvs6born",
    "lvs7born","lvs8born","lvs9born","lvs10born","lvs11born","lvs12born"], inplace=True)

# Create columns for the total number of livestock lost in the past 12 years
df["total_livestocks_lost"]=df[["lvs1lost","lvs2lost","lvs3lost","lvs4lost","lvs5lost","lvs6lost",
    "lvs7lost","lvs8lost","lvs9lost","lvs10lost","lvs11lost","lvs12lost"]].sum(axis=1)

# Drop Columns for each type of livestock lost 
df.drop(columns=["lvs1lost","lvs2lost","lvs3lost","lvs4lost","lvs5lost","lvs6lost",
    "lvs7lost","lvs8lost","lvs9lost","lvs10lost","lvs11lost","lvs12lost"], inplace=True)

# Create columns for the total number of livestock purchased in the past 12 years
df["total_livestocks_purchased"]=df[["lvs1purch","lvs2purch","lvs3purch","lvs4purch","lvs5purch","lvs6purch",
    "lvs7purch","lvs8purch","lvs9purch","lvs10purch","lvs11purch","lvs12purch"]].sum(axis=1)

# Drop Columns for each type of livestock purchased
df.drop(columns=["lvs1purch","lvs2purch","lvs3purch","lvs4purch","lvs5purch","lvs6purch",
    "lvs7purch","lvs8purch","lvs9purch","lvs10purch","lvs11purch","lvs12purch"], inplace=True)

# Create columns for the average purchase price per animal
df["livestocks_avg_purchase_price"] = df[["lvs1pprice","lvs2pprice","lvs3pprice","lvs4pprice","lvs5pprice","lvs6pprice",
    "lvs7pprice","lvs8pprice","lvs9pprice","lvs10pprice","lvs11pprice","lvs12pprice"]].mean(axis=1)

#Drop columns for purchase price per animals 
df.drop(columns=["lvs1pprice","lvs2pprice","lvs3pprice","lvs4pprice","lvs5pprice","lvs6pprice",
    "lvs7pprice","lvs8pprice","lvs9pprice","lvs10pprice","lvs11pprice","lvs12pprice"], inplace=True)

# Create columns for the average number of months than animals graze on Communalland 
df["months_grazed_communal"]=df[["lvs1graze1","lvs2graze1","lvs3graze1","lvs4graze1","lvs5graze1","lvs6graze1",
    "lvs7graze1","lvs8graze1","lvs9graze1","lvs10graze1","lvs11graze1","lvs12graze1"]].mean(axis=1)

# Drop columns with number of months each type of animals graze communal land
df.drop(columns=["lvs1graze1","lvs2graze1","lvs3graze1","lvs4graze1","lvs5graze1","lvs6graze1",
    "lvs7graze1","lvs8graze1","lvs9graze1","lvs10graze1","lvs11graze1","lvs12graze1"], inplace=True)

# Create columns for the average number of months than animals graze on 'Own land' 
df["months_grazed_own"]=df[["lvs1graze2","lvs2graze2","lvs3graze2","lvs4graze2","lvs5graze2","lvs6graze2",
    "lvs7graze2","lvs8graze2","lvs9graze2","lvs10graze2","lvs11graze2","lvs12graze2"]].mean(axis=1)

# Drop columns with number of months each type of animals graze Own land
df.drop(columns=["lvs1graze2","lvs2graze2","lvs3graze2","lvs4graze2","lvs5graze2","lvs6graze2",
    "lvs7graze2","lvs8graze2","lvs9graze2","lvs10graze2","lvs11graze2","lvs12graze2"], inplace=True)

# Create columns for the average number of months than animals graze on 'Open land' 
df["month_grazed_openland"]=df[["lvs1graze3","lvs2graze3","lvs3graze3","lvs4graze3","lvs5graze3","lvs6graze3",
    "lvs7graze3","lvs8graze3","lvs9graze3","lvs10graze3","lvs11graze3","lvs12graze3"]].mean(axis=1)

# Drop columns with number of months each type of animals graze open land
df.drop(columns=["lvs1graze3","lvs2graze3","lvs3graze3","lvs4graze3","lvs5graze3","lvs6graze3",
    "lvs7graze3","lvs8graze3","lvs9graze3","lvs10graze3","lvs11graze3","lvs12graze3"], inplace=True)

# Create columns for the total number of livestock sold in the past 12 years
df["total_livestocks_sold"]=df[["lvs1sold","lvs2sold","lvs3sold","lvs4sold","lvs5sold","lvs6sold",
    "lvs7sold","lvs8sold","lvs9sold","lvs10sold","lvs11sold","lvs12sold"]].sum(axis=1)

# Drop Columns for each type of livestock sold
df.drop(columns=["lvs1sold","lvs2sold","lvs3sold","lvs4sold","lvs5sold","lvs6sold",
    "lvs7sold","lvs8sold","lvs9sold","lvs10sold","lvs11sold","lvs12sold"], inplace=True)

# Create columns for the average sales price per animal
df["livestocks_avg_sales_price"] = df[["lvs1sprice","lvs2sprice","lvs3sprice","lvs4sprice","lvs5sprice","lvs6sprice",
    "lvs7sprice","lvs8sprice","lvs9sprice","lvs10sprice","lvs11sprice","lvs12sprice"]].mean(axis=1)

# Drop columns used for creating average sales price per animal
df.drop(columns=["lvs1sprice","lvs2sprice","lvs3sprice","lvs4sprice","lvs5sprice","lvs6sprice",
    "lvs7sprice","lvs8sprice","lvs9sprice","lvs10sprice","lvs11sprice","lvs12sprice"], inplace=True)

# Create columns for the average Quanity of livestock product used per year
df["avg_livestocks_product_used"] = df[["lvsp1use","lvsp2use","lvsp3use","lvsp4use","lvsp5use","lvsp6use",
    "lvsp7use","lvsp8use","lvsp9use"]].mean(axis=1)

# Drop columns used for creating average Quantity of liverstocks product used per year
df.drop(columns=["lvsp1use","lvsp2use","lvsp3use","lvsp4use","lvsp5use","lvsp6use",
    "lvsp7use","lvsp8use","lvsp9use"], inplace=True)

# Create columns for the average Quanity of livestock product used per year
df["avg_livestocks_product_sold"] = df[["lvsp1sell","lvsp2sell","lvsp3sell","lvsp4sell","lvsp5sell","lvsp6sell",
    "lvsp7sell","lvsp8sell","lvsp9sell"]].mean(axis=1)

# Drop columns used for creating average Quantity of liverstocks product sold per year
df.drop(columns=["lvsp1sell","lvsp2sell","lvsp3sell","lvsp4sell","lvsp5sell","lvsp6sell",
    "lvsp7sell","lvsp8sell","lvsp9sell"], inplace=True)

# Create columns for the Average Price of Livestock product sold per unit 
df["avg_product_price"] = df[["lvsp1price","lvsp2price","lvsp3price","lvsp4price","lvsp5price","lvsp6price",
    "lvsp7price","lvsp8price","lvsp9price"]].mean(axis=1)

# Drop columns used for creating average Price of Livestock product sold per unit 
df.drop(columns=["lvsp1price","lvsp2price","lvsp3price","lvsp4price","lvsp5price","lvsp6price",
    "lvsp7price","lvsp8price","lvsp9price"], inplace=True)

#Rename Columns 
df["transport_cropcost"] = df["cost1crop"] # cost of transportion of food and tree crops harvested
df["pm_cropcost"] = df["cost2crop"] # Cost of Packing/marketing of food and tree crops harvested
df["storage_cropcost"] = df["cost3crop"] # cost of storage of food and tree crops harvested
df["postharvest_croploss"] = df["cost4crop"] # Post harvest loss on food and tree crops harvested
df["other_cropcost"] = df["cost5crop"] # Other cost on food and tree crops harvested
df["transport_lvscost"]=df['cost1lvs'] # cost of transportion of livestocks
df["pm_lvscost"] = df["cost2lvs"]  #cost of Packing/marketing on livestocks
df["storage_lvscost"] = df["cost3lvs"] # cost of storage on livestock
df["postharvest_lvsloss"] = df["cost4lvs"] # Post harvest loss on livestock
df["other_lvscost"] = df["cost5lvs"] # Other cost on livestocks

# Drops columns on cost1crop,...,cost5lvs
df.drop(columns=["cost1crop","cost2crop","cost3crop","cost4crop","cost5crop","cost1lvs",
                 "cost2lvs","cost3lvs","cost4lvs","cost5lvs"], inplace=True)


# in relation to data preprocessing IV

# Created a dictionary to map old column names to new column names for renaming
column_mapping = {
    "taxincome": "income_tax",
    "taxprop": "property_tax",
    "taxsales": "sales_tax",
    "taxother": "other_tax",
    "incfarm": "net_income_farm",
    "incnfarm": "net_income_non_farm",
    "inc1r": "relatives_interest",
    "inc2r": "cooperatives_interest",
    "inc3r": "bank_interest",
    "inc4r": "loan_s_interest",
    "inc5r": "other_interest",
    "incfarm_n": "Average_income"
}

# Rename the selected columns
df.rename(columns=column_mapping, inplace=True)





