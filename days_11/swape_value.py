def swape_value(lst):
    if len(lst)>= 2:
        lst[0],lst[-1] = lst[-1],lst[0]
    return lst   

lst = [2,4,5,6,7]
print(swape_value(lst))





