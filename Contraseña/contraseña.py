#Debe incluir letras y números.
#Debe combinar letras mayúsculas y minúsculas.
#La contraseña debe incluir caracteres especiales.
#La longitud de la contraseña debe ser igual o mayor a 8 caracteres.
#No debe tener espacios en blanco.
#La contraseña generada debe mostrarse en consola y guardarse automáticamente en un archivo de texto plano.

import random
import string

# Lista con letras minúsculas, mayúsculas, números y caracteres especiales.
caracteristicas = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
#Definimos la variable en donde se tendran todos los caracteres aleatorios de la variable caract
longitud = 8
contrase = random.sample(caracteristicas, longitud)
#Pasamos esta lista a una cadena llamada password
password = "".join(contrase)

#Se define una funcion que tendra la cadena password en esta tendremos un if para verificar que se cumplan con los criterios
def generar(password):
    if (any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password) and
        len(password) >= 8 and
        not ' ' in password):
        return password
#Si la password cumple con todo la funcion devuelve la contraseña
    else:
        return generar("".join(random.sample(caracteristicas, longitud)))
#Si no se cumple con los criterios se llama de nuevo a la funcion para generar otra contraseña

password = generar(password)

print("La contraseña generada es:" + password)

archivo = open("password.txt", 'a')
archivo.write(password + '\n')


