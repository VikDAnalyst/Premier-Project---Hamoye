from Data_preprocessing import *
df=preprocessing()

# percentage of null values in all columns

# List of columns having more than 50% null values
col_to_drop=df.isna().mean().sort_values(ascending=False)[df.isna().mean()>=.20].index

# drop the selected columns
df = df.drop(col_to_drop, axis = 1)

# checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
# change incorrect datatype from float to object
# checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
# change incorrect datatype from float to object

cols_to_object=['hhcode','cadm0','cadm1','cadm2','code','farmtype','fplots','hhelectric','primary_occu',
                'sec_occu','hhrelig','lvsown','relhead']

df[cols_to_object]=df[cols_to_object].astype('object')