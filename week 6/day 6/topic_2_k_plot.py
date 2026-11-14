from sklearn.datasets import load_wine 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier 
import matplotlib.pyplot as plt

#day 5 
from sklearn.pipeline import Pipeline


X, y = load_wine(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scores = []

for k in range(1, 21):
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("model", KNeighborsClassifier(n_neighbors=k))
    ])

    pipe.fit(X_train, y_train)
    scores.append(pipe.score(X_test, y_test))


print(scores)

plt.plot(range(1, 21), scores)
plt.xlabel("K (n_neighbors)")
plt.ylabel("Accuracy")
plt.title("KNN accuracy vs K")
plt.plot(range(1, 21), scores, marker="o") #--> to see the points 
plt.show()

