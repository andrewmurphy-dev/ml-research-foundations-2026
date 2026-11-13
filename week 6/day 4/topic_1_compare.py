from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

data = load_iris(as_frame=True)

df = data.frame

#loads one full table , features and targets together

y = df["target"]
X = df.drop(columns="target")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#model 1 

model = LogisticRegression(max_iter=200)

#most steps the model can take while learning its weights ,
#200 max

model.fit(X_train, y_train)

logistic_accuracy = model.score(X_test, y_test)

print(logistic_accuracy)


#.score 

#the model guesses the specifies of the 30 test flowers , then checks its gueesses againt the real answers 

#accuracy saves the grade from 0 --> 1 





#model 2 
knn_model = KNeighborsClassifier() 

knn_model.fit(X_train, y_train)

#.fit always takes the training data


knn_accuracy = knn_model.score(X_test, y_test)



print(knn_accuracy)



#we trained two different models to guess the iris species , to see which one guesses better




#what is the difference between logistic regression and knn 


#KNN

#finds the 5 most simialr flowers it has seen 


#logistic regression 

#gives each measurement a weight , (how important it is)
#adds them up inot a score for each species 
#picks the species with the highest score 