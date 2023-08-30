# importar un modulo que realiza
import random 


def jugar_cachipum():
    print("juguemos a cachipun")
    opciones=["piedra,papel,tijera"]

    # solicitar al jugador que elija una opcion
    jugador=input("elije una opción(piedra,papel,tijera):").lower() #metodo para convertir en mayuscula
    
    # validar la opcion del jugador
    if jugador not in opciones:
        print("opcion no valida porfavor elije entre piedra,papel,tijera")
        return
    
    oponent=random.choice(opciones)#generar opcion aleatoriamente
    

