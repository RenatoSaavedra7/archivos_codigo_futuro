def suma (a,b):
    return a +b

sumar = lambda a,b : a + b

print(suma(3, 5))
print(sumar(3, 5))


numeros= [1,2,3,4,5,6]

map(numeros)

def suma (a) :
    return a + 5

nuevos_numeros = list(map(suma,numeros))
