# def sting_range(n):
#     sting = ""
#     for num in range(len(sting)):
#         sting.split(".")
#     return sting

# n = 6
# result_num  = sting_range(n)
# print(result_num)


def string_range(number):
    my_str = ""
    count = 0
    for num in range(number):
        if count == number - 1:
            my_str += str(num)
        else:
            my_str += str(num) + "."
            count += 1
    return my_str
        

n = 6
result  = string_range(n)
print("function", result, type(result))



n = 9
result = "0.1.2.3.4.5.6.7.8"

n = 4 
result = "0.1.2.3"