#question 1 


import numpy as np 

measurements = np.array([36.5, 70, 120])

print(measurements)


print(measurements.shape)


print(measurements.ndim)


#question 2 


patients = np.array([[25, 110, 68],
                     [40, 130, 75]
                     ],)

print(patients)
print(patients.shape)
print(patients.ndim)


#question 3


import numpy as np

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
])


print(data)
print(data.shape)
print(data.ndim)

#print the number of rows

print(data.shape[0])


#print the number of columns 

print(data.shape[1])