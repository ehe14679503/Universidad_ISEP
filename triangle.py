#capturo los tamaños de los lados del triángulo
a = float(input("Digite el tamaño del lado a del triángulo: "))
b = float(input("Digite el tamaño del la base del triángulo: "))
c = float(input("Digite el tamaño del lado c del triángulo: "))

#creo una variable que me sirve para identificar el tipo de triángulo
t = 0
#triángulo equilátero
if (a == b) and (b == c):
	t = 1

#triángulo isóseles
if (a == c) and (a != b):
	t = 2

#triángulo escaleno
if (a != b) and (b != c) and (a != c):
	t = 3

#valido y calculo los triángulos

#validación para el triángulo equilátero
if t == 1:
	#cálculo del área
	area = (a * b) / 2
	#imprimo el resultado
	print ("El triángulo es Equilátero y el área es: ", area)

#validación para el triángulo isóseles
if t == 2:
	#cálculo del área
	import math
	area = math.sqrt((a**2)-((b**2)/4))
	#imprimo el resultado
	print ("El triángulo es Isóseles y el área es: ", area)

#validación para el triángulo escaleno
if t == 3:
	#cálculo del área
	s = float(a+b+c)/2
	import math
	area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
	#imprimo el resultado
	print ("El triángulo es Escaleno y el área es: ", area)