#little test 

import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
])



total = matrix.sum()
#[210]
#shape has 1 element , this is called scalar


column_totals = matrix.sum(axis=0)
#[50 70 90]
#shape has 3 elements 


row_totals = matrix.sum(axis=1)
#[60 150]
#shape has 2 elements 
