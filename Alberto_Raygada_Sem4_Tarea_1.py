# Cree una función en Python que reciba tres números y retorne el mayor de los tres

mensaje = "\nA continuación se le solicitará ingresar tres \n números para retornar el mayor de ellos.\n"
print(mensaje)
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

def calcular_mayor(N1, N2, N3):
    mayor = 0
    if N1 > N2 and N1 > N3:
        mayor = N1
    elif N2 > N1 and N2 > N3:
        mayor = N2
    else:
        mayor = N3
    return mayor


mensaje = "\nEl número mayor es el: " + str(calcular_mayor(num1, num2, num3))
print(mensaje)


