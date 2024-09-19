import random

n = random.choice(range(3, 21))
unflatten_result = []

for i in range(1, n):
    for j in range(1, n):
        if n % (i + j) == 0:
            list_in_a_list = [i, j]
            if sorted(list_in_a_list) not in unflatten_result:
                unflatten_result.append(list_in_a_list)
result = [xflat for flat in unflatten_result for xflat in flat]
print(f'{n}', ' = ', *result, sep="")

