# nombre = Renato Saavedra
# definir lista de precios
precios=[250,150,300,450,200]

# 2.- ingresar descuento
while True:
   descuento = float(input("ingreso descuento a aplicar: "))
   
#3.- condición entre 0 y 100
   if 0<=descuento <= 100:
       break

   else:
        ("solo se permite el valor numérico entre 0 y 100")
    # crear función lambda para aplicar impuesto

   
    # crear funcion para aplicar impuesto
descuento_lambda= lambda num: num - (num * descuento) /100
    
# aplicar descuento utilizando map
nuevos_precios=list(map(descuento_lambda,precios))
# imprimir lista de precios originales y precios originales y precios nuevos
print(f"precios originales{precios}")
print(f"Precios con descuentos aplicados{nuevos_precios}") 