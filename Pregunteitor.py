import os
from time import *
from random import *

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def mal():
    print('mal mal mal')
clear_console()

print('Bienvenido al tipo test (responder con numeros por favor)')
Preg_inicial = input("De que lenguaje te gustaria el test?:\n1: Java\n2: Html, Css, JS.\n3: Python\n4: C++\n5: Otros\n6: Salir\nRespuesta: ")

clear_console()
while Preg_inicial != '6':
    if Preg_inicial == '1':
        clear_console()
        preg_java = int(input('Para que sirve Java?:\n1: Programacion orientada a juegos (objetos)\n2: Ciberseguridad\n3: Hacking etico\n4: Minecraft\nRespuesta: '))
        while preg_java != 1:
            clear_console()
            mal()
            preg_java = int(input('Para que sirve Java?:\n1: Programacion orientada a juegos (objetos)\n2: Ciberseguridad\n3: Hacking etico\n4: Minecraft\nRespuesta: '))
        clear_console()
        preg2_java = int(input('Que juegos fueron hechos con java\n1: Cod\n2: Minecraft\n3: Fortnite\n4: Iguanas\nRespuesta: '))
        while preg2_java != 2:
            clear_console()
            mal()
            preg2_java = int(input('Que juegos fueron hechos con java\n1: Cod\n2: Minecraft\n3: Fortnite\n4: Iguanas\nRespuesta: '))
        clear_console()
        preg3_java = int(input("Que funcion es mas utilizada en Java respecto a codigos de cualquier tipo\n1: toString()\n2: main()\n3: equals()\n4: hashCode()\n5: compareTo()\nRespuesta: "))
        while preg3_java != 2: 
            clear_console()
            mal()
            preg3_java = int(input("Que funcion es mas utilizada en Java respecto a codigos de cualquier tipo\n1: toString()\n2: main()\n3: equals()\n4: hashCode()\n5: compareTo()\nRespuesta: "))
        clear_console()
        preg4_java = int(input("Que empresa usa mas Java actual mente?:\n1: Microsoft\n2: Oracle\n3: Twitch\nRespuesta: "))
        while preg4_java != 2: 
            clear_console()
            mal()
            preg4_java = int(input("Que empresa usa mas Java actual mente?:\n1: Microsoft\n2: Oracle\n3: Twitch\nRespuesta: "))
        clear_console()
        preg5_java = int(input("Cual de estas funciones es unicamente de java:\n1: Console.log()\n2: main()\n3: def()\n4: moon()\nRespuesta: "))
        while preg5_java != 2:
            clear_console()
            mal()
            preg5_java = int(input("Cual de estas funciones es unicamente de java:\n1: Console.log()\n2: main()\n3: def()\n4: moon()\nRespuesta: "))
        clear_console()
        print('Aprobado!!')
        Preg_inicial = input("De qué lenguaje te gustaría el test?:\n1: Java\n2: Html, Css, JS.\n3: Python\n4: C++\n5: Otros\n6: Salir\nRespuesta: ")
    elif Preg_inicial == '2':
        clear_console()
        preg_html = int(input("Cuantos archivos se suelen usar para animar un hola mundo amarillo?:\n1: 1\n2: 2\n3: 3\nRespuesta: "))
        while preg_html != 3:
            clear_console()
            mal() 
            preg_html = int(input("Cuantos archivos se suelen usar para animar un hola mundo amarillo?:\n1: 1\n2: 2\n3: 3\nRespuesta: "))
        clear_console()
        preg2_css = int(input("Que se usa mas para separar en una web?\n1: CSS (gap, margin, padding...)\n2: html (br)\n3: JS\nRespuesta: "))
        while preg2_css != 1:
            clear_console()
            mal()
            preg2_css = int(input("Que se usa mas para separar en una web?\n1: CSS (gap, margin, padding...)\n2: html (br)\n3: JS\nRespuesta: "))
        clear_console()
        preg3_js = int(input("Que se usa mas en js?\n1: Animaciones\n2: Backend\n3: calculos\n4: todo lo anterior\nRespuesta: "))
        while preg3_js != 4: 
            clear_console()
            mal()
            preg3_js = int(input("Que se usa mas en js?\n1: Animaciones\n2: Backend\n3: calculos\n4: todo lo anterior\nRespuesta: "))
        clear_console()
        print('Si tenemos 4 divs y queremos cambiarles el color a todos, creamos una clase que dice "diveros" como cambiamos la clase con css?')
        preg4_css = int(input('1: ."diveros"\n2: #diveros\n3: .diveros\n4: #."diveros",#\nRespuesta: '))
        while preg4_css != 3:
            clear_console()
            mal()
            print('Si tenemos 4 divs y queremos cambiarles el color a todos, creamos una clase que dice "diveros" como cambiamos la clase con css?')
            preg4_css = int(input('1: ."diveros"\n2: #diveros\n3: .diveros\n4: #."diveros",#\nRespuesta: '))
        clear_console()
        preg5_html = int(input('que es mas utilizado en html?:\n1: div\n2: !\n3: h1\n4: todos se usan por igual\nRespuesta: '))
        while preg5_html != 1:
            clear_console()
            mal()
            preg5_html = int(input('que es mas utilizado en html?:\n1: div\n2: !\n3: h1\n4: todos se usan por igual\nRespuesta: '))
        clear_console()
        print('Aprobado!')
        Preg_inicial = input("De qué lenguaje te gustaría el test?:\n1: Java\n2: Html, Css, JS.\n3: Python\n4: C++\n5: Otros\n6: Salir\nRespuesta: ")
    elif Preg_inicial == '3':
        clear_console()
        preg_python1 = int(input("Para que es usado NORMALMENTE python\n1: Ciber\n2: Automatizacion de datos y acciones\n3: diversificacion de iguanas\n4: Pa to\nRespuesta: "))
        while preg_python1 != 1:
            clear_console()
            mal()
            preg_python1 = int(input("Para que es usado NORMALMENTE python\n1: Ciber\n2: Automatizacion de datos y acciones\n3: diversificacion de iguanas\n4: Pa to\nRespuesta: "))
        clear_console()
        from app import *
        import turtle
        square()
        triangle()
        preg2_python = int(input('Que figura sirve para hacer una casita?\n1: izquierda\n2: derecha\nRespuesta: '))
        while preg2_python != 1:
            clear_console()
            mal()
            preg2_python = int(input('Que figura sirve para hacer una casita?\n1: izquierda\n2: derecha\nRespuesta: '))
        bye()
        clear_console()
        print('Poner solo las funciones no los datos ^^')
        preg3_python = input('Si necesito crear una funcion que tenga 2 bucles 1 para que si 1 != 9 me ponga que esta mal y que si esta bien repita una piruleta 4 veces que tengo que poner?\nRespuesta: ')
        while preg3_python != 'def, while, for':
            clear_console()
            mal()
            print('Poner solo las funciones no los datos ^^')
            preg3_python = input('Si necesito crear una funcion que tenga 2 bucles 1 para que si 1 != 9 me ponga que esta mal y que si esta bien repita una piruleta 4 veces que tengo que poner?\nRespuesta: ')
        clear_console()
        preg4_python = input('Significado de POO\n1: Porimeron ordinariamente ordinario\n2: Programacion Orientada a Objetos\n3: Patos Ondulando Origuanas\nRespuesta:  ')
        while preg4_python != '2':
            clear_console()
            mal()
            preg4_python = input('Significado de POO\n1: Porimeron ordinariamente ordinario\n2: Programacion Orientada a Objetos\n3: Patos Ondulando Origuanas\nRespuesta:  ')
        clear_console()
        numero_random = randint(1, 10)
        print('Que numero estare pensando? (1-10)')
        preg5_python = int(input('Respuesta: '))
        while preg5_python != numero_random:
            clear_console()
            mal()
            print('Que numero estare pensando? (1-10)')
            preg5_python = int(input('Respuesta: '))
        print('APROBADO!!')
        clear_console()
        Preg_inicial = input("De que lenguaje te gustaria el test?:\n1: Java\n2: Html, Css, JS.\n3: Python\n4: C++\n5: Otros\n6: Salir\nRespuesta: ")
    elif Preg_inicial == '4':
        clear_console()
        preg1_cs = int(input("Que diferencia hay entre c+ de c++\n1: Las funciones\n2: El nombre\n3: los tipos de corchetes\nRespuesta: "))
        while preg1_cs != 1:
            clear_console()
            mal()
            preg1_cs = int(input("Que diferencia hay entre c+ de c++\n1: Las funciones\n2: El nombre\n3: los tipos de corchetes\nRespuesta: "))
        clear_console()
        preg2_cs = int(input("En que se especializa c++\n1: POO\n2: Dolores de cabeza\n3: aceituna\nRespuesta: "))
        while preg2_cs != 1:
            clear_console()
            mal()
            preg2_cs = int(input("En que se especializa c++\n1: POO\n2: Dolores de cabeza\n3: aceituna\nRespuesta: "))
        clear_console()
        preg3_cs = int(input("Que jeugos fueron hechos con c++\n1: Minecraft\n2: Roblox\n3: CSGO\n4: Assembly\nRespuestas: "))
        while preg3_cs != 3:
            clear_console()
            mal()
            preg3_cs = int(input("Que jeugos fueron hechos con c++\n1: Minecraft\n2: Roblox\n3: CSGO\n4: Assembly\nRespuestas: "))
        clear_console()
        preg4_cs = int(input('Porque es uno de los mas dificiles?\n1: Por el numero de funciones\n2: Por la estructura\n3: por las diferentes funciones que sirven para diversas cosas\n4: Todo lo anterior\nRespuesta: '))
        while preg4_cs != 4:
            clear_console()
            mal()
            preg4_cs = int(input('Porque es uno de los mas dificiles?\n1: Por el numero de funciones\n2: Por la estructura\n3: por las diferentes funciones que sirven para diversas cosas\n4: Todo lo anterior\nRespuesta: '))
        clear_console()
        Preg_inicial = input("De que lenguaje te gustaria el test?:\n1: Java\n2: Html, Css, JS.\n3: Python\n4: C++\n5: Otros\n6: Salir\nRespuesta: ")
    elif Preg_inicial == '5': 
        clear_console()
        print('Estas preguntas son de todo en concreto, hasta de tecnicas para programacion!!!')
        preg1_other = int(input('Que lenguaje es el mas dificil entre los siguientes\n1: Assembly\n2: Python\n3: c++\n4: C#\nRespuesta: '))
        while preg1_other != 1:
            clear_console()
            mal()
            preg1_other = int(input('Que lenguaje es el mas dificil entre los siguientes\n1: Assembly\n2: Python\n3: c++\n4: C#\nRespuesta: '))
        clear_console()
        preg2_other = int(input('Que modulo en python son mas frecuentes(en POO)\n1: Os\n2: Turtle\n3: Random\n4: Todos\nRespuesta: '))
        while preg2_other != 4:
            clear_console()
            mal()
            preg2_other = int(input('Que modulo en python son mas frecuentes(en POO)\n1: os\n2: Turtle\n3: Random\n4: Todos\nRespuesta: '))
        clear_console()
        preg3_other = int(input('Que frameworks son mas utilizados en JS para desarrollo web?\n1: React\n2: Vue\n3: Angular\nRespuestas: '))
        while preg3_other != 1: 
            clear_console()
            mal()
            preg3_other = int(input('Que frameworks son mas utilizados en JS para desarrollo web?\n1: React\n2: Vue\n3: Angular\nRespuestas: '))
        clear_console()
        preg4_other = int(input("VisualStudioCode, es un idle?:\n1: Si\n2: No\nRespuesta: "))
        while preg4_other != 2:
            clear_console()
            mal()
            preg4_other = int(input("VisualStudioCode, es un idle?:\n1: Si\n2: No\nRespuesta: "))
        clear_console()
        preg5_other = int(input('Que es un programador full Stack?:\n1: Un Programador que stakea codigo\n2: Un programador que controla de fron-end y back-end\n3: un programador que controla sobre hacking\nRespuesta: '))
        while preg5_other != 2:
            clear_console()
            mal()
            preg5_other = int(input('Que es un programador full Stack?:\n1: Un Programador que stakea codigo\n2: Un programador que controla de fron-end y back-end\n3: un programador que controla sobre hacking\nRespuesta: '))
        clear_console()
        Preg_inicial = input("De que lenguaje te gustaria el test?:\n1: Java\n2: Html, Css, JS.\n3: Python\n4: C++\n5: Otros\n6: Salir\nRespuesta: ")
    elif Preg_inicial == '6':
        clear_console()
        exit()
        Terminator()
        bye()
    elif Preg_inicial == 'AdminMode':
            clear_console()
            admin = 'megaAdmin'
            passwo = 'SoyAdmin'
            log1 = input('Usuario: ')
            while log1 != admin:
                clear_console()
                mal()
                log1 = input('Usuario: ')
            log2 = input('Password: ')
            while log2 != passwo:
                clear_console()
                mal()
                log2 = input('Password: ')
            clear_console()
            print('Bienvenido al modo admin, que desea hacer?\n1: Limpiar consola\n2: Cerrar')
            respt = int(input('Respuesta: '))
            if respt == 1:
                clear_console()
                Preg_inicial = input("De que lenguaje te gustaria el test?:\n1: Java\n2: Html, Css, JS.\n3: Python\n4: C++\n5: Otros\n6: Salir\nRespuesta: ")
            elif respt == 2:
                clear_console()
                exit()
    else:
        clear_console()
        print('no te entiendo tio!')
        Preg_inicial = input("De que lenguaje te gustaria el test?:\n1: Java\n2: Html, Css, JS.\n3: Python\n4: C++\n5: Otros\n6: Salir\nRespuesta: ")
clear_console()
exit()