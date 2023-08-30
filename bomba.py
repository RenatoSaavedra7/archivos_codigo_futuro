import time

bomba = int(input("ingrese el tiempo que debe explotar la bomba:"))

while bomba >= 8:
    print(f"la bomba estallara em :{bomba}")
    time.sleep(1)
    bomba -= 1
                    
    print("!!!BOOOOM !!! LA BOMBA EXPLOTA")


