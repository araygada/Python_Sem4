"""
Escriba una función que permita determinar si un número se encuentra en un rango determinado
ej: is_in_range(num, min, max).
"""

mensaje = "A continuación se le solicitará ingresar un número " \
          "\n y un máximo y un mínimo para determinar ." \
            "\nsi el primero se encuentra en el rango de lo dos últimos."
print(mensaje)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el número para el máximo: "))
num3 = int(input("Ingrese el número para el mínimo: "))

def en_rango(numero, max, min):
    resultado = ""
    if numero > min and numero < max:
        resultado = "El número sí está en el rango."
    else:
        resultado = "El número no está en el rango"
    return resultado

mensaje = en_rango(num1, num2, num3)
print(mensaje)