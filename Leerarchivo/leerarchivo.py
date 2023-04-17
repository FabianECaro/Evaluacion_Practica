#Contar las líneas totales del texto que se encuentra en el archivo.
#Contar las palabras totales del texto, sin contar los espacios.
#Contar los caracteres totales del texto.
#Contar el número de veces que aparece una palabra en el texto del archivo.
#Mostrar esta información en otro archivo de texto plano de salida.

#Contar el numero de lineas
q = open("archivo.txt", "r")
lineas = 0
for linea in q:
    lineas = lineas+1

print("El numero total de lineas es: ",lineas)

#Contar el numero de palabras
w = open("archivo.txt", "r")
p = w.read()
num_palabras = len(p.split())
print("El numero de palabras es: ",num_palabras)

#Contar caracteres
num_caracteres = len(p)
print("El numero de caracteres es: ",num_caracteres)

#Contar la frecuencia de palabras
frecuencia = {}
p = p.lower()
palabras = p.split()

for word in palabras:
    if word not in frecuencia:
        frecuencia[word] = 1
    else:
        frecuencia[word] += 1

resultado = open("resultado.txt", 'w')
resultado.write("Numero total de lineas es: " + str(lineas) + "\n")
resultado.write("El numero total de palabras es: " + str(num_palabras) + "\n" )
resultado.write("El numero total de caracteres es: " + str(num_caracteres) + "\n")
for palabra in frecuencia:
    totalfrecuencia = frecuencia[palabra]
    resultado.write("\n" f" La palabra '{palabra}' tiene una frecuencia de: {totalfrecuencia}")
print("La frecuencia de cada palabra es de: ")
print(f"{frecuencia}")


