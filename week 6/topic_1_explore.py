from sklearn.datasets import load_iris 

data = load_iris(as_frame=True)

df = data.frame

print(df.head())
#shows the first 5 , goes from 0 -4

print(df.describe())


print(df.shape)


#in sklearn , the y is usually callled target in datasets 


#so the shape is (150, 5) 4 features + 1 target 



#in pandas , a empty cell is called NaN 



#.isna() marks every cell True if it’s empty, False if not
#.sum() counts the Trues in each column



print(df.isna().sum())

print(df.groupby("target").mean())


