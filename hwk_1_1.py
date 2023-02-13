#!/usr/bin/env python
# coding: utf-8

# In[20]:


import requests
import json

username = input('Введите username: ') # красивый ввод юзернейма в url
username = 'obryzgalov' if username == '' else username
url = 'https://api.github.com/users/'+username+'/repos'

response = requests.get(url)
r = response.json()
print('вывод')
print(r)

repo = []
for itm in r:
    repo.append(itm['name'])
print(f'Список репок {username}')
print(repo)

with open('1_1_repo.json', 'w') as f:
    json_repo = json.dump(repo, f)


# In[ ]:





# In[ ]:




