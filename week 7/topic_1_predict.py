import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression





#day 1
def predict(X, w, b):
    return X @ w + b 


X = np.array([[2, 3],
              [4, 1]])
w = np.array([10, 5])
b = 7


result = predict(X, w, b)


print(result)

#above day 1 






data = load_diabetes(as_frame=True)

df2 = data.frame 

y = df2["target"]
X = df2.drop(columns="target")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()


model.fit(X_train, y_train)



#model.coef_, model.intercept

#model.coef_ = w, the weights, one per feature (10 for diabetes)
#model.intercept_ = b, the bias, the starting number
#So predict(X_test, model.coef_, model.intercept_) means: “use my formula, X @ w + b,



sk_preds = model.predict(X_test)
my_preds = predict(X_test, model.coef_, model.intercept_)

print("sklearn:", sk_preds[:5])
print("mine:   ", my_preds[:5].to_numpy())

#give me the first 5 items 
#.to_numpy() = “turn this into a plain NumPy array.”