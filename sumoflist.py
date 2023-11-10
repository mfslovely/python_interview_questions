# 1. Question: Write a function that takes a list of numbers and returns the sum.
# input_lst = [1, 2, 3, 4, 5]

def sum_of_list(inp_lst)-> int:
    sum_of_elements = 0
    for num in inp_lst:
        sum_of_elements += num       
    return sum_of_elements

n = [9, 2, 3, 1, 4, 8, 6]
print(sum_of_list(n))

print("list is " , sum([1,2,3,4]))

# Largest Number
# Smallest Number
# First Index Number 
# Last Index Number
# Second Last Index Number


def largest_number(n):
    max_value = n[0]
    for value in n:
        if value>max_value:
            max_value = value
    return max_value
n = [3,5,6,8,7,10,9]
print(largest_number(n)) 


def min_number(n):
    min_value = n[0]
    for num in n:
        if num<min_value:
            min_value = num
    return min_value
n = [7,1,3,5,6,0]
print(min_number(n))


lst = [1,23,45,55]
print(lst[0])
print(lst[-1])
print(lst[-2])





