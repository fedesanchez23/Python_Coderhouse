#inicialmente no lo es
valido = False

#función para validar un dato
def validar(valor):
	entero = int(valor)
	return entero >= 0 and entero <= 100
#mensaje para que el usuario sepa que le solicitamos un valor
print('Introduzca un valor, por favor: ', end='')

#bucle para pedir el valor
while not valido:
	valor = input()
	valido = validar(valor)
	if not valido:
		print('Lo siento, el valor no es válido, vuelva a intentarlo: ', end='')

#a partir de aquí sabemos que el valor es válido y ya podemos utilizarlo
print(f'El valor válido es {valor}.')