def short_lenght(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if len(lst[j]) > len(lst[j+1]):
               
               lst[j] , lst[j+1] = lst[j+1],lst[j]
    return lst
names = ['lovely','love','rajesbc']
print(short_lenght(names))
