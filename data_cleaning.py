from Data_preprocessing import *
df=preprocessing()

# percentage of null values in all columns
null_percentage = df.isnull().sum().sort_values(ascending = False)/df.shape[0]*100

# List of columns having more than 50% null values
col_to_drop = null_percentage[null_percentage>= 50].keys()

# drop the selected columns
df = df.drop(col_to_drop, axis = 1)

# checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
# change incorrect datatype from float to object
# checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
# change incorrect datatype from float to object

cols_to_object=['hhcode','cadm0','cadm1','cadm2','code','farmtype','fplots','hhelectric','primary_occu',
                'sec_occu','hhrelig','lvsown','relhead']

df[cols_to_object]=df[cols_to_object].astype('object')