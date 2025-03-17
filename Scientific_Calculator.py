#calcularora cientifica

import math
import statistics

def menu(): # Función menú
    print("\nMenú de la calculadora científica")
    print("| Opción | Descripción               |")
    print("|--------|---------------------------|")
    print("| 1      | Suma                      |")
    print("| 2      | Resta                     |")
    print("| 3      | Multiplicación            |")
    print("| 4      | División                  |")
    print("| 5      | Potencia                  |")
    print("| 6      | Raíz cuadrada             |")
    print("| 7      | Seno                      |")
    print("| 8      | Coseno                    |")
    print("| 9      | Tangente                  |")
    print("| 10     | Exponencial               |")
    print("| 11     | Residuo                   |")
    print("| 12     | Valor absoluto            |")
    print("| 13     | Promedio                  |")
    print("| 14     | Logaritmo en base 10      |")
    print("| 15     | Media aritmética          |")
    print("| 16     | Mediana                   |")
    print("| 17     | Moda                      |")
    print("| 18     | Salir                     |")
    
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if 1 <= opcion <= 18:
                return opcion
            else:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 18.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def suma(a,b):# Función suma
    return a+b  
def resta(a,b):# Función resta    
    return a-b  
def multiplicacion(a,b):# Función multiplicación
    return a*b
def division(a,b): # Función división
    return a/b
def potencia(a,b):# Función potencia
    return a**b
def raiz(a):# Función raíz cuadrada
    return math.sqrt(a)
def seno(a): # Función seno
    return math.sin(a)
def coseno(a): #
    return math.cos(a)
def tangente(a): # Función tangente
    return math.tan(a)
def exponencial(a): # Función exponencial
    return math.exp(a)
def residuo(a,b): # Residuo de la división
    return a%b
def absoluto(a):# Valor absoluto
    return abs(a)
def promedio(a,b):# Promedio de dos números
    return (a+b)/2  
def log_base10(x): # Logaritmo en base 10
    return math.log10(x)
def media_aritmetica(numeros): # Promedio de una lista de números
    return statistics.mean(numeros)
def mediana(numeros): # mediana de una lista de números
    return statistics.median(numeros)
def moda(numeros): # moda de una lista de números
    return statistics.mode(numeros)

print("Calculadora científica") # Mensaje de bienvenida
#print(menu())
while True: # Ciclo infinito de la calculadora
    opcion = menu() # Llamado a la función menú

    if opcion == 1: # Suma
        print("\nIngrese los valores a sumar:")
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        print(f"La suma de los números es: {suma(a,b)}")
        continue
        
    elif opcion == 2: # Resta
        print("\nIngrese los valores a restar:")
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        print(f"La resta de los números es: {resta(a,b)}")      
        continue
    elif opcion == 3: # Multiplicación
        print("\nIngrese los valores a multiplicar:")
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        print(f"La multiplicación de los números es: {multiplicacion(a,b)}")
        continue
    elif opcion == 4: # División
        print("\nIngrese los valores a dividir:")
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        print(f"La división de los números es: {division(a,b)}")
        continue
    elif opcion == 5:# Potencia
        print("\nIngrese los valores para la potencia:")
        a = float(input("Ingrese el valor de la base: "))
        b = float(input("Ingrese el valor del exponente: "))
        print(f"La potencia de los números es: {potencia(a,b)}")
        continue

    elif opcion in [6,7,8,9,10,12,14]: # Opciones que requieren un solo valor numérico 
        if opcion == 6:
            nombre_opcion = "raíz cuadrada"
        elif opcion == 7:
            nombre_opcion = "seno"
        elif opcion == 8:
            nombre_opcion = "coseno"
        elif opcion == 9:
            nombre_opcion = "tangente"
        elif opcion == 10:
            nombre_opcion = "exponencial"
        elif opcion == 12:
            nombre_opcion = "valor absoluto"
        elif opcion == 14:
            nombre_opcion = "logaritmo en base 10"

        a = float(input(f"Ingrese el valor para la {nombre_opcion}: ")) # Ingreso del valor numérico

        if opcion == 6:
            #print("\nIngrese el valor para la raíz cuadrada:")
            print(f"La raíz cuadrada del número es: {raiz(a)}") # Raíz cuadrada
        elif opcion == 7:
            #print("\nIngrese el valor para el seno:")
            print(f"El seno del número es: {seno(a)}") # Seno
        elif opcion == 8:
            #print("\nIngrese el valor para el coseno:")
            print(f"El coseno del número es: {coseno(a)}") # Coseno
        elif opcion == 9:
            #print("\nIngrese el valor para la tangente:")
            print(f"La tangente del número es: {tangente(a)}") # Tangente
        elif opcion == 10:
            #print("\nIngrese el valor para la exponencial")
            print(f"La exponencial del número es: {exponencial(a)}") # Exponencial
        elif opcion == 12:
            #print("\nIngrese el valor para el valor absoluto:")
            print(f"El valor absoluto del número es: {absoluto(a)}") # Valor absoluto
        elif opcion == 14:
            #print("\nIngrese el valor para el logaritmo en base 10:")
            print(f"El logaritmo en base 10 del número es: {log_base10(a)}") # Logaritmo en base 10
        continue
    elif opcion == 11: # Residuo
        print("\nIngrese los valores para el residuo:")
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        print(f"El residuo de la división de los números es: {residuo(a,b)}")
        continue
    elif opcion == 13: # Promedio
        print("\nIngrese los valores para calcular el promedio:")
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        print(f"El promedio de los números es: {promedio(a,b)}")
        continue    
    elif opcion == 15: # Media aritmética
        print("\nIngrese los números para calcular la media aritmética")
        aritmetica = []
        while True:
            numero = input("Ingrese un número (o 'X' para terminar): ")
            if numero.lower() == 'x':
                break
            aritmetica.append(float(numero))
        if aritmetica:
            print(f"\nLa media aritmética de los números es: {media_aritmetica(aritmetica)}")
        else:
            print("No se ingresaron números.")
        aritmetica.clear()  # Vaciar la lista después de la ejecución
        continue
    elif opcion == 16: # Mediana
        print("\nIngrese los números para calcular la mediana")
        Media = []
        while True:
            numero = input("Ingrese un número (o 'X' para terminar): ")
            if numero.lower() == 'x':
                break
            Media.append(float(numero))
        if Media:
            print(f"\nLa mediana de los números es: {mediana(Media)}")
        else:
            print("No se ingresaron números.")
        Media.clear()  # Vaciar la lista después de la ejecución
        continue
    elif opcion == 17: # Moda
        print("\nIngrese los números para calcular la moda")
        Moda = []
        while True:
            numero = input("Ingrese un número (o 'X' para terminar): ")
            if numero.lower() == 'x':
                break
            Moda.append(float(numero))
        if Moda:
            print(f"\nLa moda de los números es: {moda(Moda)}")
        else:
            print("No se ingresaron números.")
        Moda.clear()  # Vaciar la lista después de la ejecución
        continue
    else:
        print("\nHasta luego") # Mensaje de despedida
        break
