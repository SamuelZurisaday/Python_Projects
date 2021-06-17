#Ejemplo de High Order Functions

#Ejemplo de list comprehension
my_list = [1, 4, 5, 6, 9, 13, 19, 21]

odd = [i for i in my_list if i % 2 != 0]
print(odd)

#Ejemplo filter
my_list = [1, 4, 5, 6, 9, 13, 19, 21]

odd = list(filter(lambda x: x%2 !=0, my_list))
#Se hará una lista con la funcion filter y con la funcion anonima lambda en la que se...
#...usará una lista iterable.
print(odd)

#//////////////////////////////
#Ejemplo de list comprehension
my_list2 = [1,2,3,4,5]

squares = [i**2 for i in my_list2]
print(squares)

#Ejemplo map
my_list2 = [1,2,3,4,5]

squares = list(map(lambda x: x**2, my_list2))
print(squares)

#//////////////////////////////
#List comprehension
my_list3 = [2,2,2,2,2]

all_multiplied = 1

for i in my_list3:
    all_multiplied = all_multiplied * i

print(all_multiplied)

#Ejemplo de reduce
from functools import reduce

my_list3 = [2,2,2,2,2]
all_multiplied = reduce(lambda a, b: a * b, my_list3)

print(all_multiplied)

