from

def menu():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input())
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num



salir = False
opcion = 0

while not salir:
    print('\n                        APLICACION BOT-ARATE\n')
    print("1) Bot simple (respuestas planas...)")
    print("2) Bot simple (respuestas REGEX)")
    print("3) Bot simple mejorado desde fichero")
    print("4) Informe de la conversación(PDF)")
    print("5) Salir")

    print("Opción: ")

    opcion = menu()

if opcion == 1:

    elif opcion == 2:
    elif opcion == 3:
    elif opcion == 4:
    elif opcion == 5:
    elif opcion == 6:
salir = True
print("Cerrando programa...")