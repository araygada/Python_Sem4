"""
Cree una función que se llame round_sum(num_a, num_b, num_c). La función round_sum
recibe 3 números enteros. Para cada uno de estos números enteros, la función debe redondearlos
a la decena más cercana (ejemplo: si un número es 15, entonces se redondea a 20, pero si es 14, se
redondea a 10) y luego debe sumar los números redondeados y devolver el resultado. El
programa debe utilizar funciones de responsabilidad única por lo que debe modularizar su
solución.
"""

mensaje = "\nA continuación se le solicitarán tres números enteros, \nlos cuales se redondearán a la decena"
mensaje += " más cercana \ny se generará la suma de los números redondeados.\n"

print(mensaje)

num_a = int(input("Incluya el primer número entero: "))
num_b = int(input("Incluya el segundo número entero: "))
num_c = int(input("Incluya el tercer número entero: "))

def cal_residuo(num):
    residuo = (num * 10) / 100
    residuo = (abs(residuo) - abs(int(residuo)))
    residuo = (residuo + 0.0001) * 10
    return residuo

def cal_ajuste(numero):
    ajuste = 0
    if numero >= 5:
        ajuste = int((10 - numero) + .01)
    elif numero < 5:
        ajuste = int(numero * -1)
    return ajuste

def cal_redondeo(numero):
    valor = 0
    valor = cal_residuo(numero)
    ajuste = cal_ajuste(valor)
    redond =  numero + ajuste
    return redond

def round_sum(num_a, num_b, num_c):
    num_a = cal_redondeo(num_a)
    num_b = cal_redondeo(num_b)
    num_c = cal_redondeo(num_c)
    suma = num_a + num_b + num_c
    return suma

resultado = round_sum(num_a, num_b, num_c)

mensaje  = "La suma total de los números redondeados es: " + str(resultado)

print(mensaje)
