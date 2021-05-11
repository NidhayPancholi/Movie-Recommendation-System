def create_array(data):
    arr=np.zeros(1682)
    for x,y in data.iterrows():
        arr[y[1]-1]=y[2]
    return arr
def cosine_similarity(a,b):
    temp=np.dot(a,b)
    a=a**2
    b=b**2
    return temp/(((sum(a))**0.5)*((sum(b)**0.5)))
  
  
  def recommend_movies(sim,num_movies,user_id):
    sim.sort(key= lambda x:x[1])
    user1=df[df['user_id']==user_id]
    seen_movies=list(user1['item_id'])
    enough_movies=False
    user_movies=set()
    for x in sim[::-1]:
        temp=df[(df['user_id']==x[0]) &(df['rating'].isin([5]))]
        if len(temp)==0:
            continue
        else:
            for i,j in temp.iterrows():
                if j['item_id'] not in seen_movies:
                    user_movies.add(j['item_id'])
                if len(user_movies)==num_movies:
                    enough_movies=True
                    break
            if enough_movies:
                break
    while len(user_movies)<num_movies:
        user_movies.add(random.randint(1,1682))
    user_movies=find_movie_names(user_movies)
    seen_movies=find_movie_names(seen_movies)
    print("SEEN MOVIES",seen_movies)
    return user_movies

def find_movie_names(list_of_movies):
    names=[]
    for x in list_of_movies:
        temp=movies[movies['item_id']==x]
        names.append(list(temp['title'])[0])
    return names
