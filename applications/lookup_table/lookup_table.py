import math
import random

answer_dict = dict()
factorial_dict = dict()
modulo_dict = dict()

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    global answer_dict
    global factorial_dict
    global modulo_dict

    if answer_dict.get(str(x) + ',' + str(y)):
        return answer_dict[str(x) + ',' + str(y)]
    v = math.pow(x,y)

    if factorial_dict.get(v):
        v = factorial_dict[v]
    else:
        v = math.factorial(v)
        factorial_dict[v] = v
    v //= (x + y)

    if modulo_dict.get(v):
        v = modulo_dict[v]
    else:
        v %= 982451653
        modulo_dict[v] = v

    answer_dict[str(x) + ',' + str(y)] = v
    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
