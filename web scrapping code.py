#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# In[3]:


get_ipython().system('pip install pandas')


# In[50]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    boxes = soup.find_all("div", class_="_1AtVbE")
    
    for box in boxes:
        name_element = box.find("div", class_="_4rR01T")
        name = name_element.text if name_element else "N/A"
        Product_name.append(name)

        price_element = box.find("div", class_="_30jeq3")
        price = price_element.text.strip().replace("₹", "").replace(",", "") if price_element else "N/A"
        Prices.append(price)

        desc_element = box.find("ul", class_="_1xgFaf")
        desc = desc_element.text if desc_element else "N/A"
        Description.append(desc)

        review_element = box.find("div", class_="_3LWZlK")
        review = review_element.text if review_element else "N/A"
        Reviews.append(review)

df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Descriptions": Description, "Reviews": Reviews})
df.to_csv("flipkart_mobiles_under_50000_new2.csv", encoding="utf-8-sig")


# In[ ]:




