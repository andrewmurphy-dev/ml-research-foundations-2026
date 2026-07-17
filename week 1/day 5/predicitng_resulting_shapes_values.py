#Predict the broadcasted result shape

#for example 

#matrix.shape
# (2, 3)

#values.shape
# (1, 3)

#compare viusally 



(2, 3)
(1, 3)

#this is a little confusing 
#Your easy formula is:

#rows:    compare row numbers
#columns: compare column numbers

#At each position:

#same number → keep it
#one is 1   → keep the bigger number
#different and neither is 1 → error

#same number → works
#one is 1    → works
#anything else → fails


#the same rule applies to both rows and columns:

#for example 


#example 1

(2, 3) + (2, 3)


#2 vs 2 → match

#3 vs 3 → match

#result:

(2, 3)




#example 2


(2, 3) + (1, 3)

#2 vs 1 → 1 stretches to 2

#3 vs 3 → match

#(2, 3)




#example 3


(2, 3) + (2, 1)


#2 vs 2 → match


#3 vs 1 → 1 stretches to 3

(2, 3)



#example 4 


(4, 1) + (1, 3)


#4 vs 1 → result is 4

#1 vs 3 → result is 3


(4, 3)




#example 5

(2, 3) + (2, 2)

#2 vs 2 → works

#3 vs 2 → fails


