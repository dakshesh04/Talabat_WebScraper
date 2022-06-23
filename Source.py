#!/usr/bin/env python
# coding: utf-8

# In[20]:


from bs4 import BeautifulSoup as bs
import requests
import json
import pandas as pd
import csv 


# In[21]:


def load_data(title):
    with open(title, encoding = 'utf-8') as f:
        return json.load(f)

def save_data(title, data):
    with open(title, 'a', encoding = 'utf-8') as f:
        json.dump(data, f, ensure_ascii = False, indent=2)


# In[35]:


def menu_details(r):
    
    items_name = []
    items_des = []
    items_price = []
    items_logo = []
    R_info_list = load_data("menu.json") # load data
    page = R_info_list['pageProps']
    menu_state = page['initialMenuState']
    menu = menu_state['menuData']
    items = menu['items']
    for index,i in enumerate(items):
        items_name.append(i['name'])
        items_des.append(i['description'])
        items_price.append(i['price'])
        items_logo.append(i['image'])
    
    # Setting the details into a dataframe
    df1 = (pd.DataFrame(items_name)).transpose()
    df2 = (pd.DataFrame(items_des)).transpose()
    df3 = (pd.DataFrame(items_price)).transpose()
    df4 = (pd.DataFrame(items_logo)).transpose()
    df = df1.append(df2)
    df = df.append(df3)
    df = df.append(df4)
    df = df.transpose()  
   
    
    # saving the details to json file
    save_data('menu_list.json',r) # Restaurant's name
    save_data('menu_list.json',items_name)
    save_data('menu_list.json',items_des)
    save_data('menu_list.json',items_price)
    save_data('menu_list.json',items_logo)
    return df
    
    
def restaurant_details():
    Rest_details = {}
    R_info_list = load_data("menu.json") # load data
    page = R_info_list['pageProps']
    event = page['gtmEventData']
    rest = event['restaurant']
    Rest_details['name'] = rest['name']
    Rest_details['logo'] = rest['logo']
    Rest_details['latitude']= rest['latitude']
    Rest_details['longitude'] = rest['longitude']
    Rest_details['cuisine_tags'] = rest['cuisineString']
    csv_writer.writerow([Rest_details['name'],Rest_details['logo'],Rest_details['latitude'],Rest_details['longitude'],Rest_details['cuisine_tags']])
    save_data('Restaurant.json',Rest_details)
    return Rest_details['name']
  




# In[37]:


sample = load_data("sample.json") # using sample data
#sample = load_data("my_data.json") # Experimental data -  used on running the second time
csv_file = open('cms_scrape.csv','a')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Logo','Latitude','Longitude','Cuisine tags'])
Data_F = pd.DataFrame()
for s in sample:
    
    #print(s)
    site = (s[8:]).split('/')
    #print(site)
    countrySlug = site[1]
    vertical = site[2]
    branchId = site[3]
    payload = "aid=1308&countrySlug="+countrySlug+"&vertical="+vertical+"&branchId="+branchId
    url = "https://www.talabat.com/_next/data/0ec73ce4-edc7-45e4-a589-850f01f4a4d9/menu.json?"+payload
    print(url)
    r =requests.get(url)
    menu = r.json()
    with open("Menu.json", 'w') as f:
        json.dump(menu, f)
    
    R_name = restaurant_details()
   
    DF = menu_details(R_name)
    Data_F = Data_F.append(DF)
 # saving the dataframe to csv
Data_F.to_csv('menu_list.csv',encoding='utf-8')

csv_file.close()
csv_f2.close()
    

    
    

