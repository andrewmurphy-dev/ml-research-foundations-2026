#178 wines in total 


from sklearn.datasets import load_wine 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler 

X, y = load_wine(return_X_y=True)

#return_X_y=True) this returns the data that u want 

print(X.shape)
print(y.shape)



X_train, X_test, y_train, y_test = train_test_split(X,  y, test_size= 0.2, random_state=42)

#with test_size = 0.2 , we get 36 wines ssample f
#why do we split it into 4 piles??
#It sets some wines aside that the model never studies, so we can test it fairly on wines it hasn’t seen.

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)



#X_train contains 142 wines and 13 columns 
#y_train contains 142, 1 label for each 142 wines 




model = KNeighborsClassifier()



model.fit(X_train, y_train)

#this is the "studying step", .fit 
#it just memorises all 142 training wines and their types, so it can compare new wines to them later.

test_score = model.score(X_test, y_test)
#so this is the important part 
#.score does 3 things 

#1 guesses 36 wines in X_test 
#2 marks compares the 36 guesses to real answers in y_test 
#3 return a fraction from 0 - 1 

print("Accuracy without scaling:", test_score)


#answer is 0.75 

#0.75 * 36 = 26 correct out of 36 



#remmeber this always tells yoy how many items are along each direction of an array 


#what do u mean by scaling 

#Scaling means changing the numbers in each column so they’re all on a similar size, without changing what they tell you


#so next we need to scale the data 




scaler = StandardScaler() 



#what does standard scalar do ?
#For each column, work out that column’s mean (across the 142 training wines).
#Subtract that mean from every value in that column, to see how far away from the average it is 
#Divide every value in that column by that column’s std.
#after that every column is centered around 0 
#it doesnt change the order 


scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
#transform does the actual calculation ,(value − column mean) ÷ column std

X_test_scaled = scaler.transform(X_test)



model_scaled = KNeighborsClassifier()

model_scaled.fit(X_train_scaled, y_train)


scaled_test_score = model_scaled.score(X_test_scaled, y_test)

print("Accuracy with scaled:", scaled_test_score)



#so scaling does change the numbers themselves , and the distances change 