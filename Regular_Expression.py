#!/usr/bin/env python
# coding: utf-8

# # NLP: Regular Expressions

# Regex in customer support chatbot

# Retrieve order number

# In[1]:


import re


# In[39]:


chat1 = 'codebasics:Hello, I am having an issue with my order # 421889912'
chat2 = 'codebasics:I have a problem with my order number 412889912'
chat3 = 'codebasics: My order 212889923 is having a issue, I was charged  300$ when online it says 280$'


# In[35]:


pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat1)
matches


# In[36]:


matches = re.findall(pattern, chat2)
matches


# In[37]:


matches = re.findall(pattern, chat3)
matches


# Retrieve email id and phone

# Email Id

# In[41]:


chat1 = 'codebasics: you ask lot of questions  1235678912, abcA@xyz.com'
chat2 = 'codebasics: here it is (123)-567-8912, abc@xyz.com'
chat3 = 'codebasics: yes, phone: 1235678912 email: abc@xyz.com'


# In[42]:


pattern = '[a-z0-9A-Z_]*@[a-z0-9A-Z]*\.com[a-zA-Z]*'

matches = re.findall(pattern, chat1)
email = matches[0]
email


# In[43]:


matches = re.findall(pattern, chat2)
email = matches[0]
email


# In[44]:


matches = re.findall(pattern, chat3)
email = matches[0]
email


# Phone Number

# In[45]:


pattern = '\d{10}|\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern, chat1)
matches


# In[46]:


pattern = '\d{10}|\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern, chat2)
matches


# In[47]:


pattern = '\d{10}|\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern, chat3)
matches


# (2) Regex for Information Extraction

# In[49]:


text='''
Born	Elon Reeve Musk
June 28, 1971 (age 50)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa (1971–present)
Canada (1971–present)
United States (2002–present)
Education	University of Pennsylvania (BS, BA)
Title	
Founder, CEO and Chief Engineer of SpaceX
CEO and product architect of Tesla, Inc.
Founder of The Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI, and Zip2
Spouse(s)	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''


# In[50]:


pattern = 'age (\d+)'
matches = re.findall(pattern, text)
matches


# In[51]:


pattern = 'Born(.*)'
matches = re.findall(pattern, text)
matches[0].strip()


# In[52]:


pattern = 'Born.*\n(.*)\(age'
matches = re.findall(pattern, text)
matches[0].strip()


# In[53]:


pattern = '\(age.*\n(.*)'
matches = re.findall(pattern, text)
matches[0].strip()


# In[54]:


def get_pattern_match ( pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]


# In[55]:


get_pattern_match ('\(age.*\n(.*)', text)


# In[56]:


def get_personal_information(text):
    age = get_pattern_match('age (\d+)', text)
    full_name = get_pattern_match('Born(.*)\n', text)
    birth_date = get_pattern_match('Born.*\n(.*)\(age', text)
    birth_place = get_pattern_match('\(age.*\n(.*)', text)
    return {
        'age': int(age),
        'name': full_name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
    }


# In[57]:


get_personal_information(text)


# In[ ]:





# In[ ]:




