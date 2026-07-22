#so what is .iloc?

#this is selecting by index psotion , not label like in loc!
#think iloc as index loc 

#for example 

import pandas as pd 

students = pd.DataFrame(
    {
        "name": ["Andy", "Sarah", "Ken"],
        "score": [80, 92, 75]
    },
    index=["a", "b", "c"]
)



print(students)

print(students.loc["a"])


print(students.iloc[0])

