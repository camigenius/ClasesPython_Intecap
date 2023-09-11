current_number = 1

while current_number <= 4 :
    print(current_number)
    current_number += 1


prompt = "\n Para salir de este programa debera digitar la palabra 'quit '"

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)



prompt = "\n Por favor Ingrese la ciudad que tu quieres Visitar y para que se detenga  el programa por favor ingresar 'quit' "


while True:
    city = input(prompt)

    if city == 'quit':
        break

    else :
        print(f"yo deseo ir a {city.title()} por que es muy bonita ")


# script simular acceso a cuenta bancaria utilizado un password y que al 3 intento
# me saque del programa y me diga que la clave bloqueado por seguridad








