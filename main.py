from models.nube import Nube
# nombre = input("Ingrese el nombre del archivo por favor: ")
# access_token: str = input("Ingrese el token de acceso (dropbox): ")
# nube: Nube = Nube(nombre, access_token)
# nube.msg("Ingrese 2 numeros para dividir")
# num1 = float(input("Numero 1: "))
# num2 = float(input("Numero 2: "))
#
# if num2 == 0:
#     nube.error("No es posible dividir entre 0")
# elif int(num1 / num2) <= 0:
#     nube.advertencia(f"El resultado puede ser un numero muy pequeño: {num1/num2}")
# else:
#     nube.exito(f"Resultado: {num1/num2}")

nombre_1 = input("Ingrese el nombre del archivo por favor: ")
access_token_1: str = input("Ingrese el token de acceso (dropbox): ")
nombre_2 = input("Ingrese el nombre del archivo por favor: ")
access_token_2: str = input("Ingrese el token de acceso (dropbox): ")

nube: Nube = Nube(nombre_1, access_token_1)
nube2: Nube = Nube(nombre_2, access_token_2)

if nube == nube2:
    print('Son iguales')
else:
    print('No son iguales')
