from Data_preprocessing import *
df=preprocessing()

# percentage of null values in all columns

# List of columns having more than 50% null values
col_to_drop=df.isna().mean()[df.isna().mean()>=.50].index

# drop the selected columns
df = df.drop(columns=col_to_drop)

# checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
# change incorrect datatype from float to object
# checked incorrect datatypes from first column(hhcode) to column 35(sickdays)
# change incorrect datatype from float to object

cols_to_object=['hhcode','cadm0','cadm1','cadm2','code','farmtype','fplots','hhelectric','primary_occu',
                'sec_occu','hhrelig','lvsown','relhead', 'water_supply', 'season2_water_supply']

<<<<<<< HEAD
df[cols_to_object]=df[cols_to_object].astype('object')

#trying for Seyi
||||||| 7990993
df[cols_to_object]=df[cols_to_object].astype('object')
=======
df[cols_to_object]=df[cols_to_object].astype('object')
>>>>>>> b1f422a228a0994f30cdb24ccda10c7a08685f20
