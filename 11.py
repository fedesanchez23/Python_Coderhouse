
# def area_recatangulo(base,altura):
#     area = (base * altura)
#     return area

# base = int(input("Ingrese un valor para la base: "))
# altura = int(input("Ingrese un valor para la altura: "))

# rectangulo = area_recatangulo(base,altura)

# print(f"El area del rectangulo es {rectangulo}")


# import math
# pi = math.pi

# from math import pi



# def area_circulo(radio):
#         return pi * (radio**2)


# radio = float(input("Ingrese un valor para el radio: "))

# print(f"El area del circulo es {area_circulo(radio)}")

# def relacion(n1, n2):
#     if n1 > n2:
#         return 1
#     elif n1 < n2:
#         return -1
#     return 0
 
# print(relacion(5, 5))
# print(relacion(10, 5))
# print(relacion(5, 10))

# n1 = int(input("Ingrese un número: "))
# n2 = int(input("Ingrese otro número: "))

# def intermedio(n1, n2):
#         return (n1 + n2) / 2
 
# print(f"el intermedio de los números ingresados es {intermedio(n1, n2)}")



# numero = int(input("Ingrese un número: "))
# limite_inferior = int(input("Ingrese el limite inferior: "))
# limite_superior = int(input("Ingrese el limite superior: "))

# def recortar(numero, limite_inferior, limite_superior):
#     if numero < limite_inferior:
#         return limite_inferior
#     elif numero > limite_superior:
#         return limite_superior
#     else:
#         print(f"el numero ingresado {numero} esta dentro de los limites")

# print(recortar(numero, limite_inferior, limite_superior))


numeros = [-12, 84, 13, 20, -33, 101, 9]
def separar(*arg):
    lista = sorted(arg)
    pares = []
    impares = []
    for arg in lista:
        if arg % 2 == 0:
            pares.append(arg)
        else:
            impares.append(arg)
        
    return pares, impares
 
pares, impares = separar(*numeros)
print(pares)   
print(impares)




