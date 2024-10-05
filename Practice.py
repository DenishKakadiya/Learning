
list = list(range(11))

my_gen = (n*n for n in list)

print(my_gen)
print(type(my_gen))
print(type(range(11)))