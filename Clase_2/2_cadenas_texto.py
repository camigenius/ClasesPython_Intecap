print("Hola mundo")

cadenamultiple = """
Por favor Ingresa una frase este
programa cuenta el número de palabras 
que tiene la frase
"""

print(cadenamultiple)

text = input("Ingresa la frase : ")

# print(len(text))

count_text = len(text)
text_replace= text.replace(" ","") # reeplaza texto o caracter por otro dentro de una cadena de texto
count_text_replace = len(text_replace)

print(count_text)
print(count_text_replace)

espace = count_text - count_text_replace
print(f"La frase que ingresate tiene {espace+1} palabras")








