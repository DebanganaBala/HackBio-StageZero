#!/usr/bin/env python
# coding: utf-8

# # Group Project - HackBio

# In[1]:


#Importing Pandas
import pandas as pd

#Creating dictionary with Column names (key) and Adding Member information next to each Column name (Values)
data = {
  "Name": ["Svetlana","Santosh","Debangana","Gideon Danso","Mosunmola Temitope Christianah","Hana E"],
  "Slack Username": ["Svetlana Sokolova","Santosh T","Debangana","Joegidi4real","Temmy","Hana E"],
  "Country" :["United Kingdom","United States of America","United Kingdom","Ghana","Nigeria","Canada"],
  "Hobby":["Playing Piano","Tennis","Badminton","Listening to music","Cooking","Hiking"],
  "Affiliation":["Queens University Belfast","University of Texas at San Antonio","Queens University Belfast (Alumna)","University of Cape Coast","Obafemi Awolowo University","Boise State University"],
  "Favourite Gene (gene name)":["TP53","IFNB","BRCA1","BRCA2","TNNT2","glnD"]
}

#Converting the dictionary to Dataframe with custom row names for better clarity 
df = pd.DataFrame(data, index = ["Member 1", "Member 2", "Member 3","Member 4","Member 5","Member 6"])
 

#Saving the dataframe as a csv file
df.to_csv('data.csv', index= True)


#Read the CSV file and use the first column as index 
df = pd.read_csv("data.csv", index_col=0)
print(df)


# In[ ]:




