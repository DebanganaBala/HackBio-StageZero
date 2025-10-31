#!/usr/bin/env python
# coding: utf-8

# # Group Project - HackBio

# In[4]:


#Importing Pandas
import pandas as pd

#Creating dictionary with Column names (key) and Adding Member information next to each Column name (Values)
data = {
  "Name": ["Svetlana","Santosh","Debangana","Gideon Danso"],
  "Slack Username": ["Svetlana Sokolova","Santosh T","Debangana","Joegidi4real"],
  "Country" :["United Kingdom","United States of America","United Kingdom","Ghana"],
  "Hobby":["Playing Piano","Tennis","Badminton","Listening to music"],
  "Affiliation":["Queens University Belfast","University of Texas at San Antonio","Queens University Belfast (Alumna)","University of Cape Coast"],
  "Favourite Gene (gene name)":["TP53","IFNB","BRCA1","BRCA2"]
}

#Converting the dictionary to Dataframe with custom row names for better clarity 
df = pd.DataFrame(data, index = ["Member 1", "Member 2", "Member 3","Member 4"])
 

#Saving the dataframe as a csv file
df.to_csv('data.csv', index= True)


#Read the CSV file and use the first column as index 
df = pd.read_csv("data.csv", index_col=0)
print(df)


# In[ ]:




