import getpass

password = getpass.getpass("ingrese su contraseña: ")

# en este caso vamos a definir password como hola mundo
# mientras la contraseña no sea hola mundo seguira solicitando

while password != "hola mundo":
    password = getpass.getpass("la clave es incorrecta.Ingrese nuevamente: ")
    print("la clave es correcta.puedes utilizar tu programa")
   