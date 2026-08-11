#Conditional Probability.



#What is the probability of something happening, given that we already know something else is true?



#for example 


#Imagine a class has:
#10 students total

#6 are women
#4 are men

#Out of the 6 women:
#3 wear glasses


#normally we would ask !
#What is the probability a random student wears glasses?



#but if we ask 

#what is the probability a student wears glasses,
#GIVEN that the student is a woman?

#we no longer care about all 10 students

#3 women wear glasses
#6 women total

#probability = 3 / 6
#            = 0.5
#            = 50%


#“given that” = reduce the group you are looking at.


#question 1 

#there are 8 animals , 5 dogs , 3 cats 
#Out of the 5 dogs, 2 are black.

#What is the probability that an animal is black given that it is a dog?


probability = 2 / 5

percentage = probability * 100

print(percentage)

print(round(percentage, 1))