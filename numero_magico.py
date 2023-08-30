import random

def jugar_numero_magico():
    intentos=3
    numero= random.randint(0,50)

    while intentos > 0:
        seleccion_usuario= int(input(f"Tienes"))