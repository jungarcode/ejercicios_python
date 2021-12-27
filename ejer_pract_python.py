cadena =input('Escribe una frase: ')
while cadena != '':
  cambios = 0
  for i in range(1, len(cadena)):
    if cadena[i] == ' ' and cadena[i-1] != ' ':
      cambios = cambios + 1

  if cadena[-1] == ' ':
    cambios = cambios - 1

  palabras = cambios + 1
  print('Palabras:', palabras)

  cadena =input('Escribe una frase: ')
  
def abs_lista(lista):
      for i in range(len(lista)):
        lista[i] = abs(lista[i])

milista = [1, -1, 2, -3, -2, 0]
abs_lista(milista)
print(milista)

# suma de numeros de 1 al 6

n=6
suma=0
i=1
while i <=n:
  suma=suma+i
  i=i+1
print("la suma de los numeros hasta",str(n),"es: ", str(suma)) 

#tabla de multiplicar

n=int(input("introduce la tabla de deseas ver: "))
i=1
a=10
while i <= a:
      print(n,"x",str(i),"=",str(n*i))
      i=i+1
print("la tabla resuelta") 

# for numero de vocales de una frase

frases=str(input("ingrese una frase; "))

vocales = str("aeiouAEIOU")

contador=0
for i in frases:
  if i in vocales:
    contador= contador+1          
print("el numero de vocales es: ",str(contador))

# tbla de multiplicar con for

n=int(input("introduca la tabla que deseea: "))

for i in range(1,11):
      print(n,"x",str(i),"=",str(n*i))
print("resultado de la tabla que solicitaste")      

#sumatoria de todos los numeros de 0 a 100

total=0
for i in range(101):
      total=total+i
print("la sumatori= ",str(total))      
      
      
"""Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente."""

numero = int(input("introduce numero impar: "))

while numero % 2 == 0:
      numero = int(input("introduce numero impar: "))
      
"""1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:** \n",
    "* Mostrar una suma de los dos números\n",
    "* Mostrar una resta de los dos números (el primero menos el segundo)\n",
    "* Mostrar una multiplicación de los dos números\n",
    "* En caso de no introducir una opción válida, el programa informará de que no es correcta."""


n1=int(input("ingresa primer numero: "))

n2=int(input("ingresa segundo numero: "))

opcion= 0

print("que quieres hacer: \n", "1. sumar los 2 numeros\n","2. restar los 2 numeros\n","3. multiplicar los 2 numeros")
opcion = int(input("introduce el numero: "))

if opcion == 1:
      sumar=n1+n2
      print("la suma es: ",sumar)
elif opcion == 2:
      restar=n1-n2
      print("la resta es: ",restar)
elif opcion== 3:
      multiplicar=n1*n2
      print("la multiplicacion es: ",multiplicar)
else:
      print("opcion incorrecta")
      
        
print("gracias")

"""3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:**\n",
    "\n",
    "*Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.*"""
    
suma=sum(range(0,101,2))
print(suma)    

n=0
suma=0

while n<=100:
  if n%2==0:
    suma=suma+n
  n=n+1
print(suma)    

"""4) Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:**\n"""

suma=0
numero = int(input("cuntos numeros quiere introducir: "))

for i in range(numero):
    suma=suma+int(input("introduce los numeros: "))
print("se ha introducido el total de numero: ",numero,"\nla suma de los numeros es: ",suma,"\nla media artmetica es: ",suma/2)    

"""5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:**\n",
    "\n",
    "*Consejo: La sintaxis \"valor in lista\" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)*"""
    
numeros = [1,3,6,9]

while True:
      numero=int(input("introduce un numero entre 0 y 9: "))
      if numero>=0 and numero<=9:
        break
      
if numero in numeros:
  print("el numero: ",numero, "se encuentra en la lista de ",numeros)
else:
  print("el ", numero, "no se encuentra en la lista de ", numeros)  
  
  
"""Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno en uno.
Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30."""


num = int(input("ingrese un numero:"))

x=1

while x<=num:
  print(x)
  x= x+1
  
"""Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio."""

x=1
suma=0
while x<=10:
  valor = int(input("ingrese valor= "))
  suma+=valor
  x+=1
prom = suma/10
print("la suma total es")
print(suma)
print("el promedio total es")
print(prom)

"""Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote."""

x=1
cantidad=0
n=int(input("cuantas piezas va procesar:"))

while x<=n:
  long = float(input("ingrese la longitud:"))
  if long >=1.20 and long<=1.30:
    cantidad+=1
  x=x+1

print("la cantidad de piezas actas son")  
print(cantidad)   

"""Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores."""
 
x=1
contBajas=0
contAltas=0

while x<=10:
  nota=int(input("ingrese nota:"))
  if nota>=7:
    contAltas+=1
  else:
    contBajas+=1
  x+=1  
  
print("cantidad de alumnos con notas mayores a 7") 
print(contAltas)
print("cantidad de alumnos con notas menores a 7") 
print(contBajas)  
  
      
"""Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas."""

x=1
suma=0
n=int(input("cuantas personas se van a medir: "))
while x<=n:
  valorAltura=float(input("ingrese la altura de cada persona:"))
  suma+=valorAltura
  x+=1
prom=suma/n

print("el promedio de las alturas es")
print(prom)  
  
"""En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal. """

x=1
sueldoAltos=0
sueldoBajos=0
suma=0
n=int(input("cuantos trabajadores hay en la empresa:"))

while x<=n:
  sueldo=float(input("introduce el sueldo de cada empleado"))
  if sueldo>=100 and sueldo<=300:
    sueldoBajos+=1
  else:
    sueldoAltos+=1
  x+=1
  suma=suma+sueldo 
 
gasto=suma

print("la cantidad de trabajadores q cobran entre 100 y 300")
print(sueldoBajos)
print("la cantidad de trabajadores q cobran mas de 300")
print(sueldoAltos)
print("el gasto total de la empresa es")
print(gasto)

"""Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)"""

serie=11
x=1
while x<=25:
  print(serie)
  serie+=11
  x+=1
  
  
"""Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc"""

multiplo8=8
while multiplo8<=500:
  print(multiplo8)
  multiplo8+=8
 