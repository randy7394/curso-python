###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
os.system("clear")

# print("\n Sentencia simple condicional")

# edad = 18
# if edad >= 18:
#   print("Eres mayor de edad")
#   print("¡Felicidades!")

# edad = 15
# if edad >= 18:
#   print("Eres mayor de edad")
#   print("¡Felicidades!")

# print("\n Sentencia condicional con else")
# edad = 15
# if edad >= 18:
#   print("Eres mayor de edad")
# else:
#   print("Eres menor de edad")

# print("\n Sentencia condicional con elif")
# nota = 5

# if nota >= 9:
#   print("¡Sobresaliente!")
# elif nota >= 7:
#   print("Notable!")
# elif nota >= 5:
#   print("¡Aprobado!")
# else:
#   print("¡No está calificado!")

# print("\n Condiciones múltiples")
# edad = 16
# tiene_carnet = True

# # JavaScript
# # && -> and
# # || -> or

# # un pueblo de Valencia
# if edad >= 18 and tiene_carnet:
#   print("Puedes conducir ")
# else:
#   print("POLICIA !!!1!!!")

# # un pueblo de Isla Margarita
# if edad >= 18 or tiene_carnet:
#   print("Puedes conducir en la Isla Margarita ")
# else:
#   print("Paga al policía y te deja conducir!!!")

# es_fin_de_semana = False
# # JavaScript -> !
# if not es_fin_de_semana:
#   print("¡midu, venga que hay que streamear!")

# print("\n Anidar condicionales")
# edad = 20
# tiene_dinero = True

# if edad >= 18:
#   if tiene_dinero:
#     print("Puedes ir a la discoteca")
#   else:
#     print("Quédate en casa")
# else:
#   print("No puedes entrar a la disco")

# # Más fácil:
# # if edad < 18:
# #   print("No puedes entrar a la disco")
# # elif tiene_dinero:
# #   print("Puedes ir a la discoteca")
# # else:
# #   print("Quédate en casa")

# numero = 5
# if numero: # True
#   print("El número no es cero")

# numero = 0
# if numero: # False
#   print("Aquí no entrará nunca")

# nombre = ""
# if nombre:
#   print("El nombre no es vacío")

# numero = 3 # asignación
# es_el_tres = numero == 3 # comparación

# if es_el_tres:
#   print("El número es 3")


# print("\nLa condición ternaria:")
# # es una forma concisa de un if-else en una línea de código
# # [código si cumple la condición] if [condicion] else [codigo si no cumple]

# edad = 17
# mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
# print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
# print("\nEjercicio 1:")
# num1 = int(input("Introduce el primer numero: "))
# num2 = int(input("Introduce el segundo numero: "))

# if num1 > num2:
#   print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#   print(f"{num2} es mayor que {num1}")
# else:
#   print("Los numeros son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
# print("\nEjercicio 2")
# num1 = float(input("Introduce el primer numero: "))
# num2 = float(input("Introduce el segundo numero: "))
# operacion = input("Indica el tipo de operacion que deseas realizar (+, -, *, /): ")

# if operacion == "+":
#     resultado = num1 + num2
# elif operacion == "-":
#     resultado = num1 - num2
# elif operacion == "*":
#     resultado = num1 * num2
# elif operacion == "/":
#   if num2 == 0:
#       print("Oye, no se puede dividir entre 0")
#   else:
#       resultado = num1 / num2
# else:
#   print("No se lo que me has pedido")

# if 'resultado' in locals():
#   print(f"El resultado es: {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
# print("\nEjercicio 3:")
# anio = int(input("Introduce un año: "))

# if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#   print(f"{anio} es un año bisiesto.")
# else:
#   print(f"{anio} no es un año bisiesto.")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print("\nEjercicio 4:")
edad = int(input("Introduce una edad: "))

if 0 <= edad <= 2:
  print("Bebe")
elif 3 <= edad <= 12:
  print("Niño")
elif 13 <= edad <= 17:
  print("Adolescente")
elif 18 <= edad <= 64:
  print("Adulto")
elif edad >= 65:
  print("Tercera edad")
else:
  print("No se lo que me has dicho")