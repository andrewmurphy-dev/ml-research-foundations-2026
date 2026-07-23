#here we just filter rows 

import pandas as pd 

movies = pd.DataFrame({
    "title": ["Alien", "Titanic", "Shrek", "Jaws"],
    "rating": [8.5, 7.9, 7.8, 8.1],
    "year": [1979, 1997, 2001, 1975]
})


#first lets create a boolean series 

print(movies["rating"] >= 8)


#0     True
#1    False
#2    False
#3     True
#Name: rating, dtype: bool
#remember this creates a series 

high_rated = movies[movies["rating"] >= 8]

print(high_rated)


#   title  rating  year
#0  Alien     8.5  1979
#3   Jaws     8.1  1975


#when filtered as above it does not create a series 

#formula DataFrame[Boolean condition] → filtered DataFrame


#practice questions 


#question 1 
games = pd.DataFrame({
    "title": ["Zelda", "Mario", "Halo", "Tetris"],
    "score": [95, 88, 82, 91]
})


#Create a Boolean Series checking which games have a score of at least 90.
condition = games["score"] >= 90 
print(condition)

high_scores = games[condition]
print(high_scores)




