from itertools import count, cycle

# ----------a----------------
my_list = []
z = 1
for i in count(3):
    if i > 10:
        break
    else:
        my_list.append(i)
        print(i)
# ----------b----------------
for i in cycle(my_list):
    if z > 8:
        break
    print(i)
    z += 1
