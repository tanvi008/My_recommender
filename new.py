import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import process
 
movies = pd.read_csv('/home/tanvirupareliya/Desktop/movie recommender/tmdb_5000_movies.csv',usecols = ['id','title'], dtype= {'id ': 'int32', 'title':'str'} )
ratings = pd.read_csv('/home/tanvirupareliya/Desktop/movie recommender/ratings.csv',usecols = ['userId','movieId','rating'], dtype ={'userId':'Int64','movieId':'Int64','rating':'float'})

df_movies = movies
df_ratings = ratings

df_movies.head()
df_ratings.head()

movies_user = df_ratings.pivot(index = 'movieId',columns ='userId', values='rating').fillna(0)
mat_movies_user = csr_matrix(movies_user.values) 
x = mat_movies_user

model_knn = NearestNeighbors(metric ='cosine',algorithm ='brute', n_neighbors=20)
model_knn.fit(mat_movies_user)


def recommender(movie_name,data=x, model=model_knn, n_recommendations=20):

    model.fit(data)
    idx = process.extractOne(movie_name,df_movies['title'])[2]
    print('Movies Selected: ',df_movies['title'][idx], 'Index: ',idx)
    print('----------------Your Recommendations are----------------')
    distances , indices=model.kneighbors(data[idx], n_neighbors = n_recommendations)
    for i in indices:
        return_df = (df_movies['title'][i].where(i!=idx))

    return return_df



print(recommender("Avatar"))