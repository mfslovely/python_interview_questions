def only_floats(a,b):
    if isinstance(a,float) and isinstance(b,float):
        return 2
    elif isinstance(a,float) or isinstance(b,float):
        return 1
    else:
        return 0

result = only_floats(12.7, 23.7)

print(result)
