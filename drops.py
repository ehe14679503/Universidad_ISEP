#obtengo el número a calcular los factores primos
n = int(input("Digite el número:"))
#la variable b la utilizo para imprimir la cantidad ingresada si no es 3, 5 o 7
b = n
#la variable a me sirve para saber si cumplió con las condiciones de tener un factor primo 3, 5 o 7
a = 0
#construyo el array para los factores primos
primos2 = []
#for que comienza en 2 hasta llegar al número ingresado
for i in range(2, n+1):
	#while que permite validar las condiciones de los factores primos y si el factor es 3,5 o 7 lo agrego al array
	while n % i == 0:
		#valido si el factor primo es 3
		if (i) == 3:
			#cambio la variable a en 1
			a = 1
			#agrego al array la palabra de gota correspondiente al número del factor primo
			primos2.append('Plic')
			#valido si el factor primo es 5
		if (i) == 5:
			#cambio la variable a en 1
			a = 1
			#agrego al array la palabra de gota correspondiente al número del factor primo
			primos2.append('Plac')
			#valido si el factor primo es 7
		if (i) == 7:
			#cambio la variable a en 1
			a = 1
			#agrego al array la palabra de gota correspondiente al número del factor primo
			primos2.append('Ploc')
		#divido el numero del factor primo con el número igresado el cual se va dividiendo a medida que pasa por al for hasta finalizar
		n = n / i
#valido si el número ingresado no cumple con la condición de tener 3, 5 o 7 como factor primo
if a == 0:
	#agrego al array el número ingresado ya que no cumplió con la condición de tener 3, 5 o 7 como factor primo
	primos2.append(b)
#imprimo el contenido del array
print(primos2)