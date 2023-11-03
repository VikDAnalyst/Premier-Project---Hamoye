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