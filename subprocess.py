#!/usr/bin/env python3

import subprocess

# solo una demostracion de como funciona subprocess para correr comandos y almacenar el output en variables
# faltaria trabajar en el formato de la salida para comandos cuya salida es detallada por ejemplo: ls -alh
# con comandos sencillos tipo "ls" podria ser mas facil trabajar con la salida

def main():
    
    #print("""write your commnad with or without arguments like "ls -alh"\n""")
    try:
        #process = subprocess.Popen(subprocess.sys.argv[1:], stdout=subprocess.PIPE)
        #process.communicate()
        subprocess.Popen(subprocess.sys.argv[1:])
        # Aqui hay algo interesante, si quitamos los corchetes de argv dejandolo 'subprocess.sys.argv" tal cual, entra en un ciclo infinito
        # something fun is: if you leave just argv withouth brackets, the program falls into an infinite loop
        exit(0)
    except IndexError:
        print("Faltan argumentos: {subprocess.sys.argv[0]} [comando como lo escribiria en linea de comandos]")

if __name__ == '__main__':
    main()
