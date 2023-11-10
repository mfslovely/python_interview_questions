def check_duplicates(lst):
    dublicate = []
    set_1 = set()
    for value in lst:
        if value in set_1 and value not in dublicate:
            dublicate.append(value)
        else:
            set_1.add(value)
    if len(dublicate) > 0:
        return list(dublicate)
    else:
        return "No duplicates"

lst_1 = ["banana", "orrange", "apple"]

reult_lst = check_duplicates(lst_1)
print(reult_lst)