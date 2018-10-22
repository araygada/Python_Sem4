"""
Escriba una función en Python que permita determinar si un número es perfecto o no. Un
número perfecto es un número entero positivo cuyo valor es igual a la suma de todos sus divisores
enteros positivos. (https://es.wikipedia.org/wiki/Número_perfecto)
"""

mensaje = "\nA continuación deberá incluir un número y \nse le indicará si es un número perfecto o no.\n"

print(mensaje)

num = int(input("Incluya un número entero : "))

# Determina los divisores del número
def divisores(numero):
    lista = []
    for i in range(1, num):
        residuo = 0
        resultado = num / i
        residuo = (resultado - int(resultado))
        if residuo == 0:
            lista.append(i)
    return lista

# Determina la suma de los divisores del número
def suma_divisores(numero):
    Lista_divisores = []
    Lista_divisores = divisores(numero)
    suma = 0
    for i in Lista_divisores:
        suma += i
    return suma

# Determina si es o no un número perfecto
def perfecto(numero):
    if suma_divisores(numero) == numero:
        mensaje = str( numero) + " sí es un número perfecto"
    else:
        mensaje = str(numero) + " no es un número perfecto"
    return mensaje

mensaje = ""
mensaje =perfecto(num)

print(mensaje)

