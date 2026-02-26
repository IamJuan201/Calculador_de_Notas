#Aqui defino colores (por añadir):
import os
AZUL = '\033[94m'
CIAN = '\033[96m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
RESET = '\033[0m'
NEGRITA = '\033[1m'

#limpiar pantalla para que no aparezca lo anterior (por añadir)

#Esta es la interfaz del programa:
while True:
    print(f"╔" + "═"*58 + "╗")
    print(f"║" + "CALCULADOR DE NOTAS".center(58) + "║")
    print(f"╚" + "═"*58 + "╝")
    nombre = input("Escribe tu nombre: ")

    print(f"Hola {nombre}! Bienvenido a tu calculadora de notas")
    print("─"*60)
    print("1. Calcular promedio de notas")
    print("2. Salir")
    print()
    opcion = input("Escribe la opcion que deseas hacer (1-2): ")
    print("─"*60)

#Aqui se recogen los datos de notas y se hacen los procesos:
    try:
        if opcion == '1':
            nota_1 = float(input("Digite su primera nota: "))
            nota_2 = float(input("Digite su segunda nota: "))
            nota_3 = float(input("Digite su tercera nota: "))

            promedio = (nota_1 + nota_2 + nota_3)/3

            print("─"*60)
            print(f"{nombre} según tus notas: ")
            print(nota_1)
            print(nota_2)
            print(nota_3)
            print()
            print("─"*60)
            print("tu promedio es:", round(promedio, 2))
            print("─"*60)

#Finalizar programa
        elif opcion == '2':
            print("Gracias por usar la calculadora, Hasta pronto!")
            break
        else:
            print()
            print()
            print("ERROR! Esa opcion no existe")
#Errores
    except ValueError:
        print()
        print()
        print(f"ERROR! Digite solo numeros, EJ: 4; 4.7; 3.0")

    