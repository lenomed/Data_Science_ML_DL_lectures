import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style('white')

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\u.data', sep='\t', names=column_names)

movie_titles = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\Movie_Id_Titles')
movie_titles.head()

df = pd.merge(df,movie_titles,on='item_id')
#print(df.head())

#sns.heatmap(df.isnull())
#plt.show()
 
df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
df.groupby('title')['rating'].count().sort_values(ascending=False).head()

moviemat = df.pivot_table(index='user_id', columns='title',values='rating')
print(moviemat.head())

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())

ratings['num of ratings'] = df.groupby('title')['rating'].count()

#print(ratings.head())

#print(ratings.sort_values('num of ratings', ascending=False).head())

starwars_user_ratings = moviemat['Star Wars (1977)']
liar_liar = moviemat['Liar Liar (1997)']
print(starwars_user_ratings)

star_correlations = moviemat.corrwith(starwars_user_ratings)
print(star_correlations)

liar_correlations = moviemat.corrwith(liar_liar)

print(liar_correlations)

corr_starwars = pd.DataFrame(star_correlations, columns=['Correlations'])
corr_starwars['num of ratings'] = ratings['num of ratings']

print(corr_starwars.sort_values(by='Correlations', ascending=False).head())
corr_starwars.dropna(inplace=True)
print(corr_starwars.head())

sort_ratings = corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlations',ascending=False).head()
print(sort_ratings)