#so here we will do some practcie questions ! 

import numpy as np 

numbers = np.array([5, 10, 15, 20])



final_answer = numbers[numbers * 4]
print(final_answer)

#this is wrong actually ! 

#You wrote:

numbers[numbers * 4]

#NumPy does this first:

numbers * 4
# [20, 40, 60, 80]

#Then it reads your code as:

numbers[[20, 40, 60, 80]]

#That means:

#Select positions 20, 40, 60, and 80.

#But your array only has positions:

0, 1, 2, 3

#So it crashes.

#The correct code is:

final_answer = numbers * 4

#Because you are not selecting anything. You are transforming every value.

#The exact rule is:

numbers[...]  → select values
numbers * 4   → multiply values




#Yes. They are index positions.

numbers[[20, 40, 60, 80]]

#means:

#Select the values stored at index positions 20, 40, 60, and 80.

#But your array:

numbers = np.array([5, 10, 15, 20])

#only has:

index:  0   1   2   3
value:  5  10  15  20

#So indexes 20, 40, 60, and 80 do not exist.