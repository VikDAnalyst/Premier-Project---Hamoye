
from Data_preprocessing import *
df=preprocessing()

# percentage of null values in all columns

# List of columns having more than 50% null values
col_to_drop=df.isna().mean()[df.isna().mean()>=.50].index

# drop the selected columns
df = df.drop(columns=col_to_drop)

# checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
# change incorrect datatype from float to object

cols_to_object=['hhcode','cadm0','cadm1','cadm2','code','farmtype','fplots','hhelectric','primary_occu',
                'sec_occu','hhrelig','lvsown','relhead', 'water_supply', 'season2_water_supply']

df[cols_to_object]=df[cols_to_object].astype('object')

#which seasons suffered more loss among the two seasons? 

import matplotlib.pyplot as plt
df[['season1_mean_loss','season2_mean_loss']].mean().plot(kind='barh')
#from the mean loss comparison barchart, season2 suffered more loss with a mean loss of 592.87 than season1 with a mean loss of 443.21