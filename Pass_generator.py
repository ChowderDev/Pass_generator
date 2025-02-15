# primero importaremos las librerias a utilizar

import random
import string
import pyperclip

# vamos a pedirle al usuario que ingrese la longitud de la contraseña
while True:
    print("                     🔐 Bienvenido al generador de contraseñas! 🔐")
    print("         🔑 La longitud de la contraseña debe estar entre 4 y 20 caracteres. 🔑")
    print("🔑 La contraseña generada puede contener letras mayusculas, minusculas, numeros y simbolos. 🔑\n")

    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))
    except ValueError:
        print("⚠️ Aviso: La longitud debe ser un numero entero.")
        continue  # Si ocurre un error, le pedimos nuevamente la longitud

    if longitud < 4 or longitud > 20:
        print("⚠️ Aviso: La longitud debe estar entre 4 y 20 caracteres.")
        continue  # Si la longitud no esta en el rango, le pedimos nuevamente la longitud
    else:
        print(f"🔑 Generando contraseña de {longitud} caracteres... aguarde un momento por favor.")

#ahora vamos a definir los caracteres que se van a utilizar para generar la contraseña
#los caracteres que vamos a utilizar son los siguientes:
#letras mayusculas, minusculas, numeros y simbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation

#ahora vamos a generar la contraseña
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

#ahora vamos a preguntarle al usuario si desea copiar la contraseña al portapapeles
    respuesta = input("Desea copiar la contraseña al portapapeles? (s/n): ")

    if respuesta.lower() == "s":
        pyperclip.copy(contrasena)
        print("✅ Contraseña copiada al portapapeles!")
    else:
        print(f"🔑 Contraseña: {contrasena}")

#ahora vamos a preguntarle al usuario si desea generar otra contraseña
    respuesta = input("Desea generar otra contraseña? (s/n): ")

    if respuesta.lower() != "s":
        print("👋 Gracias por usar el generador de contraseña.")
        break
