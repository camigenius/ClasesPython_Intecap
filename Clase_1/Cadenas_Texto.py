# Ejercicio No 1


cadenamultiple = '''
    Por Favor Ingresa una Frase este programa
    cuenta el numero de palabras que contiene
    una frase
'''

print(cadenamultiple)

frase = input("Ingresa una frase : ")

frase_sin_espacios = frase.replace(" ","")

print(len(frase))
print(len(frase_sin_espacios))



numeroletrasfrase = len(frase) - len(frase_sin_espacios)

print("EL Numero de palabreas en la frase es :",numeroletrasfrase +1)


