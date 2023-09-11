my_range = range(6)

print(my_range)

print(list(my_range))

# rango(inicio,fin,pasos o saltos)

print(list(range(3,8)))
print(list(range(-10,11,1)))


print("**********Example 1 ************")

for number in range(5):
    print(number)


print("**********Example 2 ************")

for number in range(3,8):
    print(number)

print("**********Example 3 ************")
for i in range(-15,10,3):
    print(i)    

people = ['Milnea','Emma','Tomas','Julio','Camilo']


for i in (people.range(0,5,2)):
    print(i)