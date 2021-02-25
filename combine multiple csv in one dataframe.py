#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import glob
import pandas as pd
os.chdir("/mydir") # Folder Path

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in a dataframe 
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])


# In[7]:


combined_csv


# In[ ]:




