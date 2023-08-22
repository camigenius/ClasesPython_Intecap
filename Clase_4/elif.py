list_pet = ['dog','cat','fish']
print(list_pet)

pet = input("De la anterior lista de python que mascota eligirias : ")

pet = pet.lower()

if pet in list_pet:

    if pet  == 'dog':
        print('Genial los perros son muy lindos!')
    if pet == 'cat':
        print("Chevere pero son muy independientes y dañan las sillas")

    if pet == "fish":
        print("Muy territoriales y hay que tenerlos separados segun la especie")

else :
    print("Debes Ingresar de manera correcta tu elección tal cuál como esta en la lsita")



list_pet = ['dog','cat','fish']
print(list_pet)

pet = input("De la anterior lista de python que mascota eligirias : ")

pet = pet.lower()

if pet in list_pet:
    if pet == "dog":
        print('Genial los perros son muy lindos!')
    elif pet == 'cat':
        print('Chevere pero son muy independientes y dañan las sillas') 
    elif pet == 'fish' :
        print('Muy territoriales y hay que tenerlos separados segun la especie')      
 
else :
    print("Debes Ingresar de manera correcta tu elección tal cuál como esta en la lsita")





