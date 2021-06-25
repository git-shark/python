a = 100
b = a
print(b)
a = 200
print(b)
print(a)

list_a = [0, 1, 2]
list_b = list_a
print(list_b)
list_a = [10, 11, 12]
print(list_b)

list_c = list_a
print(list_c)
list_a[1] = 101
print(list_c)