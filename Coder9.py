def anio_bisiesto(anio):
    if anio % 4 == 0:
        return  "es bisiesto"
    elif anio % 400 == 0:
      return  "es bisiesto"
    elif anio % 100 == 0:
        return "no es bisiesto"
    else:
      return "no es bisiesto"

anio = int(input("ingrese un año: "))

# continuar = True

# while continuar:

#     anio = input("ingrese un año: ")

#     if anio != type(int):
#         continuar = print("debe ingresar un año")
    


print("El año " + str(anio) + " " + str(anio_bisiesto(anio)))