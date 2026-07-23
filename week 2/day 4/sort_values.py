#.sort_values() rearranges the rows based on one column.


#for example 

import pandas as pd

movies = pd.DataFrame({
    "title": ["Alien", "Titanic", "Shrek", "Jaws"],
    "rating": [8.5, 7.9, 7.8, 8.1]
})




sorted_movies = movies.sort_values("rating")

print(sorted_movies)



#     title  rating
#2    Shrek     7.8
#1  Titanic     7.9
#3     Jaws     8.1
#0    Alien     8.5


#the structure 


#movies.sort_values("rating")
#│                    │
#DataFrame          column used for sorting




#default is assending , lowest to highest 


#practice question 



#question 1 

games = pd.DataFrame({
    "title": ["Zelda", "Mario", "Halo", "Tetris"],
    "score": [95, 88, 82, 91]
})

sort_games = games.sort_values("score")
print(sort_games)


#    title  score
#2    Halo     82
#1   Mario     88
#3  Tetris     91
#0   Zelda     95




#question 2 

games = pd.DataFrame({
    "title": ["Zelda", "Mario", "Halo", "Tetris"],
    "score": [95, 88, 82, 91]
})


#so here we will learn desc ! 

result = games.sort_values("score", ascending=False)

#ascending=False means highest → lowest

print(result)


#    title  score
#0   Zelda     95
#3  Tetris     91
#1   Mario     88
#2    Halo     82