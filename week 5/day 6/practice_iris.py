from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


#day 6 


from sklearn.metrics import accuracy_score 
from sklearn.metrics import confusion_matrix

#import the data 




X, y = load_iris(return_X_y=True)
#load the data 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#so you go 150 * 0.2 = 30 
#fixes the shuffle, random state comes out the exact same every time u run it , the data 
#42 is the number u choose for it 




model = KNeighborsClassifier() 

model.fit(X_train, y_train)

model_test_score = model.score(X_test, y_test)

print("accuracy without scaling:", model_test_score)




scaler = StandardScaler()

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)

X_test_scaled = scaler.transform(X_test)



#then we do the scaled version of the model 


model_scaled = KNeighborsClassifier()

model_scaled.fit(X_train_scaled, y_train)

scaled_test_score = model_scaled.score(X_test_scaled, y_test)


print("Accuracy with scaled: ", scaled_test_score)


#day 6 part 


#predict()
#seeing what the model predicted before seeing what it got right in comparision to y_test

y_prediction = model.predict(X_test)

print(y_prediction)


#[1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0]


#next we do accuracy 


accuracy = accuracy_score(y_test, y_prediction)



print(accuracy)




#confusion matrix

print(confusion_matrix(y_test, y_prediction))