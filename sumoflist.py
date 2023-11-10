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


print("===================================================================================================================")

# 2. Question: How do you reverse a string in Pythons?

message = "Hello India"

print(message[::-1])

print("===================================================================================================================")

# Question: How can you remove duplicates from a list?

def dublicate_number(s):
    dublicate_value={}
    
    for number in s:
        if number not in dublicate_value:
            dublicate_value[number] = 1
        else:
            dublicate_value[number] += 1
    return dublicate_value
s = [1,2,4,4,6,7,7]
print(dublicate_number(s))

print("===================================================================================================================")



# How do you handle exceptions in Python?
# we can use try except blockes for haddle Exception

a = 1
b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("can not divide by zero")

print("===================================================================================================================")

#  What is a lambda function? Provide an example.
# lamba function is small anomous function . it is takes any number of arugument but have one expresion

x = lambda a,b,c : a+b+c
print(x(1,2,3))
print("===================================================================================================================")


# 11. Question: What is list comprehension and provide an example?


square_list = [x**2 for x in range(10)]
print(square_list)
print("="*100)




def find_digit(number):
    lst = []  
    while(number>0):
        a = number%10
        lst.append(a)
        number = number//10
    return lst

number = 123
result_value = find_digit(number)
print(result_value)


#power of two
print("*" * 100)
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


number = 6
count = 0
while(number>0):
    if number % 2 == 0:
        number = number // 2
        # print(number,"hello")
        if number == 1:
            print(f"Number is power of 2")
            break
    else:
        print(f"Number is not power of 2")
        break