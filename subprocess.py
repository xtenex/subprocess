#!/usr/bin/env python3

import subprocess

# solo una demostracion de como funciona subprocess para correr comandos y almacenar el output en variables
# faltaria trabajar en el formato de la salida para comandos cuya salida es detallada por ejemplo: ls -alh
# con comandos sencillos tipo "ls" podria ser mas facil trabajar con la salida

def main():
    
    #print("""write your commnad with or without arguments like "ls -alh"\n""")
    try:
        subprocess.Popen(subprocess.sys.argv[1:])
        exit(0)
    except IndexError:
        print("Faltan argumentos: {subprocess.sys.argv[0]} [comando como lo escribiria en linea de comandos]")

if __name__ == '__main__':
    main()
