#what is this ??


#applying one operation to an entire array without writing the element-by-element Python loop yourself.



#NumPy still processes the elements, but the looping happens internally in fast compiled code.


#REMEMBER THIS 
#Vectorization expresses repeated element operations as a single array operation.


#so python loop version you know this ! 


numbers = [10, 30, 50]

result = []


for num in numbers:
    result.append(numbers * 2)

print(result) 


#but for the numpy version 


import numpy as np 


numbers = np.array([10, 30, 50])

result = numbers * 2

print(result)



#you give numpy one instruction !

#Multiply the entire array by 2.


#Python instruction
#       ↓
#NumPy operation
#       ↓
#compiled internal loop
#       ↓
#[20, 40, 60]



#Vectorization moves repetitive element-by-element work from a Python-level loop into a NumPy array operation implemented in compiled code.




num = np.array([10, 40, 50, 33])

multiply_num = num * 2


print(multiply_num.shape)
print(multiply_num)

#(4,)
#[ 20  80 100  66]



#so its interesting in day 2 we done boolean masks !



import numpy as np 


numbers = np.array([10, 45, 66, 700])

mask = numbers >= 30

print(mask)
print(mask.dtype)

#so this doesnt select the values , only the boolean values 



#so if you want to select the values !

result = numbers[mask]
print(result)

#[ 45  66 700]






num = np.array([10, 40, 50, 33])

greater = num > 30

print(greater)
print(greater.dtype)



#[False  True  True  True]
#bool

#if you want to get values 


jam = num[greater]
print(jam)

#[40 50 33]

#so the values need ssquare brackets not ()


#there is a shorter version to write this , what you have is a longer version ! 


jams = np.array([10, 45, 55, 55])

result = jams[jams >= 30]
print(result)

#[45 55 55]



#REMEMBER THIS APPLIES TO ALL THINGS IN NUMPY !!!!!!

numbers + 5
numbers * 2
numbers / 10
numbers ** 2

numbers > 30
numbers <= 100
numbers == 20




np.sqrt(numbers)
np.abs(numbers)
np.round(numbers)



array1 + array2
array1 * array2



#my confusion is when do we use SQUARE BRACKETS?

#array[...] means select data from the array.

#array[...] means: use whatever is inside the square brackets as instructions for which elements to select from the array.


#for example 


jams = np.array([10, 45, 55, 55])

result = jams[jams >= 30]


numpy first:
jams >= 30


then 
[False, True, True, True]


jams[[False, True, True, True]]



False → do not select
True  → select
True  → select
True  → select


[45 55 55]



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



#I AM JUST GETTING CONFUSED WHEN TO USE SHORTER VERSION 



result = numbers[numbers >= 30]

#means:

#Select the values located at positions where numbers >= 30 is True.

#Example:

numbers = np.array([5, 10, 35, 50])

#The comparison creates:

#position:   0      1      2     3
#condition: False  False  True  True

#Then:

#result = numbers[numbers >= 30]

#returns the values at the True positions:

#[35 50]



#SO IN SUMMERY WHEN DO I MAKE THIS ??????

result = numbers[numbers >= 30]



#when i just want to make a compairsion ??

numbers > value
numbers >= value
numbers < value
numbers <= value
numbers == value
numbers != value

numbers[(numbers >= low) & (numbers <= high)]
numbers[(numbers < low) | (numbers > high)]
numbers[~(numbers >= value)]
