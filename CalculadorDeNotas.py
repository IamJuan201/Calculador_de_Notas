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
    print(f"{CIAN}╔" + "═"*58 + "╗")
    print(f"║" + f"{RESET}{NEGRITA}CALCULADOR DE NOTAS".center(66) + f"{RESET}{CIAN}║")
    print(f"╚" + "═"*58 + "╝")
    nombre = input(f"{RESET}{NEGRITA}Escribe tu nombre: {RESET}{VERDE}")

    print(f"{RESET}{NEGRITA}Hola {RESET}{VERDE}{nombre}{RESET}{NEGRITA}! Bienvenido a tu calculadora de notas{RESET}")
    print(f"{CIAN}─{RESET}"*60)
    print(f"{ROJO}1. {RESET}{NEGRITA}Calcular promedio de notas")
    print(f"{ROJO}2. {RESET}{NEGRITA}Salir")
    print()
    opcion = input(f"Escribe la opcion que deseas hacer {ROJO}(1-2){RESET}{NEGRITA}:{RESET} {VERDE}")
    print(f"{CIAN}─{RESET}"*60)

#Aqui se recogen los datos de notas y se hacen los procesos:
    try:
        if opcion == '1':
            print(f"{RESET}{NEGRITA}Ingresa tus notas {ROJO}(0-5) {RESET}")
            print()

            nota_1 = float(input(f"{NEGRITA}Digite su primera nota:{RESET}{VERDE} "))
            while nota_1<0 or nota_1>5:
                print(f"{ROJO}ERROR! Solo se permiten numeros del 0 al 5{RESET}")
                nota_1 = float(input(f"{NEGRITA}Digite su primera nota:{RESET}{VERDE} "))

            nota_2 = float(input(f"{RESET}{NEGRITA}Digite su segunda nota:{RESET}{VERDE} "))
            while nota_2<0 or nota_2>5:
                print(f"{ROJO}ERROR! Solo se permiten numeros del 0 al 5{RESET}")
                nota_2 = float(input(f"{NEGRITA}Digite su segunda nota:{RESET}{VERDE} "))

            nota_3 = float(input(f"{RESET}{NEGRITA}Digite su tercera nota:{RESET}{VERDE} "))
            while nota_3<0 or nota_3>5:
                print(f"{ROJO}ERROR! Solo se permiten numeros del 0 al 5{RESET}")
                nota_3 = float(input(f"{NEGRITA}Digite su tercera nota:{RESET}{VERDE} "))

            nota_min = 3.0
            promedio = (nota_1 + nota_2 + nota_3)/3

            print(f"{RESET}{CIAN}─{RESET}"*60)
            print(f"{VERDE}{nombre}{RESET}{NEGRITA} según tus notas: {RESET}{NEGRITA}")
            print(nota_1)
            print(nota_2)
            print(nota_3)
            print()
            if promedio>=nota_min:
                print(f"{RESET}{CIAN}─{RESET}"*60)
                print(f"{NEGRITA}tu promedio es: {RESET}{VERDE}{round(promedio, 2)}{RESET}")
                print()
                print(f"{AMARILLO}Enhorabuena si pasaste :D{RESET}")
                print(f"{CIAN}─{RESET}"*60)
            elif promedio<nota_min:
                print(f"{CIAN}─{RESET}"*60)
                print(f"tu promedio es: {ROJO}{round(promedio, 2)}{RESET}")
                print()
                print(f"{AMARILLO}Debes estudiar mas... no pasaste :({RESET}")
                print(f"{CIAN}─{RESET}"*60)

#Finalizar programa
        elif opcion == '2':
            print(f"{VERDE}Gracias por usar la calculadora, Hasta pronto!{RESET}")
            break
        else:
            print()
            print()
            print(f"{ROJO}ERROR! Esa opcion no existe{RESET}")
#Errores
    except ValueError:
        print()
        print()
        print(f"{ROJO}ERROR! Digite solo numeros, EJ: 4; 4.7; 3.0{RESET}")

    