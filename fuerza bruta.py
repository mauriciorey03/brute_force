import time
import sys

while True: 
    password = list(input("Ingrese una palabra clave de 4 letras: ")) #Por ahora solo letras minúsculas
    if len(password)==4:
        break
    else:
        print("Por favor intente con una palabra de 4 letras.")

alfabeto=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#caracteres=['{', '}', '[', ']', '(', ')', '*', ';', '/', ',', '_', '-']
seguir=True
inicio = time.time()
input("Presione Enter para continuar...")


for c1 in alfabeto:
    intento = [c1]
    print(c1)
    if intento == password:
        print("Clave encontrada: ", intento)
        input()
        final = time.time()
        print("Tiempo consumido: {:5.2f}".format(final-inicio))
        sys.exit()
    for c2 in alfabeto:
        intento = [c1,c2]
        print(c1,c2)
        if intento == password:
            print("Clave encontrada: ", intento)
            input()
            final = time.time()
            print("Tiempo consumido: {:5.2f} seg".format(final-inicio))
            sys.exit()
        for c3 in alfabeto:
            intento = [c1,c2,c3]
            print(c1,c2,c3)
            if intento == password:
                print("Clave encontrada: ", intento)
                input()
                final = time.time()
                print("Tiempo consumido: {:5.2f} seg".format(final-inicio))
                sys.exit()
            for c4 in alfabeto:
                intento = [c1,c2,c3,c4]
                print(c1,c2,c3,c4)
                if intento == password:
                    print("Clave encontrada: ", intento)
                    input()
                    final = time.time()
                    print("Tiempo consumido: {:5.2f} seg".format(final-inicio))
                    sys.exit()