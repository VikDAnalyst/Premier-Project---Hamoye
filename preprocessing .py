#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns',40)


# In[2]:


df = pd.read_csv('data.csv')


# In[3]:


#sum the eduation of the members of each household to determine the level education in each.
df['edu_level'] = df[df.columns[df.columns.str.contains('educ')]].sum(axis = 1)


# In[4]:


df['edu_level'].head(5)


# In[5]:


#drop educ1 - educ38
df.drop(df.columns[df.columns.str.contains('educ')], axis = 1, inplace = True)


# In[6]:


#aggregate the ages of each household to determine the strength and level of experience

#average age of each household
df['ave_age'] = df[df.columns[df.columns.str.contains('age')]].mean(axis = 1)

#maximum age
df['max_age'] = df[df.columns[df.columns.str.contains('age')]].max(axis = 1)

#drop age1 - age38
#df.drop(df.columns[df.columns.str.contains('age')], axis = 1, inplace = True)

df.drop(['age1','age2', 'age3', 'age4', 'age5', 'age6', 'age7', 'age8', 'age9', 'age10','age11', 'age12', 'age13', 'age14', 'age15',
                   'age16', 'age17', 'age18', 'age19', 'age20', 'age21', 'age22', 'age23', 'age24', 'age25', 'age26', 'age27', 'age28',
                   'age29', 'age30', 'age31', 'age32', 'age33', 'age34', 'age35', 'age36', 'age37', 'age38'], axis = 1, inplace = True)


# In[ ]:





# In[7]:


#to determine the number of female and male in each household
df['nmale'] = df[df.columns[df.columns.str.contains('gender')]].apply(lambda x: (x == 1).sum(), axis = 1)



df['nfemale'] = df[df.columns[df.columns.str.contains('gender')]].apply(lambda x: (x == 2).sum(), axis = 1)


#drop gender1 - gender38
df.drop(df.columns[df.columns.str.contains('gender')], axis = 1, inplace = True)


# In[8]:


#frequency of members involve in non farmwork
df['mem_nfarmwrk'] = df[df.columns[df.columns.str.contains('nfarmwork')]].apply(lambda x : (x == 1).sum(), axis = 1)


#drop nfarmwork1 - 38
df.drop(df.columns[df.columns.str.contains('nfarmwork')], axis = 1, inplace = True)


# In[9]:


#frequency of member involve in farmwork
df['mem_farmwrk'] = df[df.columns[df.columns.str.contains('farmwork')]].apply(lambda x : (x == 1).sum(), axis = 1)

#drop farmwork1 - 38
df.drop(df.columns[df.columns.str.contains('farmwork')], axis = 1, inplace = True)


# In[10]:


#married

#number of married people
df['n_maried'] = df[df.columns[df.columns.str.contains('married')]].apply(lambda x : (x== 1).sum(), axis =1)

#number of singles
df['n_singles'] = df[df.columns[df.columns.str.contains('married')]].apply(lambda x : (x== 2).sum(), axis =1)

#number of divorceds
df['n_divorced'] = df[df.columns[df.columns.str.contains('married')]].apply(lambda x : (x== 3).sum(), axis =1)

#number of teengers
df['n_teengers'] = df[df.columns[df.columns.str.contains('married')]].apply(lambda x : (x== 4).sum(), axis =1)


#drop married1 - 38
df.drop(df.columns[df.columns.str.contains('married')], axis = 1, inplace = True)


# In[ ]:





# In[11]:


#rename primary occupation and secondary occupation
df = df.rename({'hhhdocc1' : 'primary_occu', 'hhhdocc2' : 'sec_occu'}, axis = 1)


# In[12]:


df[['hhcode', 'hhsize', 'hhtribe', 'hhrelig','hhelectric', "n_maried", 'n_divorced', 'n_teengers','n_singles', 'edu_level', 'ave_age', 'max_age', 'nmale', 'nfemale', 'occ1days','primary_occu', 'sec_occu',
   'occ1wks', 'occ2days', 'occ1wks', 'sickdays', "mem_farmwrk", 'mem_nfarmwrk']].head(5)


# In[13]:


df.head(5)


# In[ ]:




