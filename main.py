import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

movies=pd.read_csv("/kaggle/input/dataset/Movie_Id_Titles.csv")
df=pd.read_csv("/kaggle/input/dataset/Dataset.csv")
df.head()

  
similarity={}
thresh=0.3
all_users=df['user_id'].unique()
for user1 in all_users:
    temp1=df[df['user_id']==user1]
    arr1=create_array(temp1)
    similarity[user1]=[]
    for user2 in all_users:
        if user2!=user1:
            temp2=df[df['user_id']==user2]
            arr2=create_array(temp2)
            sim=cosine_similarity(arr1,arr2)
            if sim>thresh:
                similarity[user1].append((user2,sim))
                
recommend_movies(similarity[196],10,196)
recommend_movies(similarity[0],10,0)
