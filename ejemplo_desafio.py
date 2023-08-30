
# definir lista de precios
precios=[500,300,200,800,400]

# 2.- ingresar descuento
while True:
    impuesto = float(input("ingreso impuesto a aplicar: "))
   
#3.- condición entre 0 y 100
    if 0<=impuesto <= 100:
       break

    else:
        ("solo se permite el valor numérico entre 0 y 100")
    # crear función lambda para aplicar impuesto

   
    # crear funcion para aplicar impuesto
impuesto_lambda= lambda num: num + (num * impuesto) /100
    # impuesto_lambda= lambda 250: 250 +(250*10)/100

# aplicar descuento utilizando map
nuevos_precios=list(map(impuesto_lambda,precios))
# imprimir lista de precios originales y precios originales y precios nuevos
print(f"precios originales{precios}")
print(f"Precios con impuestos aplicados{nuevos_precios}") 