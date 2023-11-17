from emoji import emojize

def Python_snakes(n: int):

    for i in range(0, n):

        for j in range(n, i, -1):
                    print(end=" ")
        for k in range(0, i):
                print(emojize(':snake:'), end=" ")
        print("\n")

Python_snakes(7)