from Data_preprocessing import *
df=preprocessing()

# percentage of null values in all columns
null_percentage = df.isnull().sum().sort_values(ascending = False)/df.shape[0]*100
null_percentage

# List of columns having more than 50% null values
col_to_drop = null_percentage[null_percentage>= 50].keys()
col_to_drop

# drop the selected columns
df = df.drop(col_to_drop, axis = 1)
# checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
# change incorrect datatype from float to object
df['hhcode'] = df['hhcode'].astype(object)
df['cadm0'] = df['cadm0'].astype(object)
df['cadm1'] = df['cadm1'].astype(object)
df['cadm2'] = df['cadm2'].astype(object)
df['code'] = df['code'].astype(object)
df['farmtype'] = df['farmtype'].astype(object)
df['fplots'] = df['fplots'].astype(object)
df['hhelectric'] = df['hhelectric'].astype(object)
df['primary_occu'] = df['primary_occu'].astype(object)
df['sec_occu'] = df['sec_occu'].astype(object)
df['hhrelig'] = df['hhrelig'].astype(object)
df['lvsown'] = df['lvsown'].astype(object)
df['lvsown'] = df['lvsown'].astype(object)
df['relhead'] = df['relhead'].astype(object)
