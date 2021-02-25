#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2


# In[2]:


file = open('path', 'rb')
pdfr = PyPDF2.PdfFileReader(file)

pdfr.numPages

page = pdfr.getPage(0)

txt = page.extractText()

txt

file.close()


# In[6]:





# In[ ]:




