# summation = 0
# starting_index = 1
# index = starting_index
# maximum_index = 100

# while index < maximum_index:
#     summation += 1/index

# print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

# Errors:
# indexing over index but index value doesn't change

#Examination of values by hand (rather, excel) reveals 2nd error, in that maximum_index being set at 100 stops the code from adding the final 1/100 value necessary for the actual correct computation of the sum. 
#This can be corrected by changing while statement to while index < maximum_index + 1.

# LLM Comment: (Using replit's ai)
#The issue with the given code is that the index variable is not updated within the while loop. To fix this, you can increment the index variable by 1 in each iteration of the loop. Here's the corrected code:
# (LLM's) corrected code simply adds index+=1 line into while loop

# Corrected Code:
summation = 0
starting_index = 1
index = starting_index
maximum_index = 100

while index < maximum_index+1:
    summation += 1/index
    index += 1

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')