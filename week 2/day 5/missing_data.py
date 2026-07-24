import pandas as pd

students = pd.DataFrame({
    "name": ["Andy", "Sarah", "Ken", "Mia"],
    "score": [80, 92, None, 88]
})

print(students)


#missing data 



#NaN means missing value

#so we use this arument , isna(). returns:

#True  → missing
#False → not missing

#it goes through every element and asks Is this value missing?

print(students.isna())


#0  False  False
#1  False  False
#2  False   True
#3  False  False


#.isna() only detects missing values.
#It does not remove them.
#It does not replace them.



#Andy   → name exists, score exists
#Sarah  → name exists, score is missing
#Ken    → name exists, score exists