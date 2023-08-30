# ventana
wn = turtle.Screen()
wn.title("Juego ping pong")
wn.bgcolor("green")
wn.setup(width= 800, height= 600) #ancho por alto
wn.tracer() #para ver que fluja bien

# marcador
marcadorA= 0
marcadorB= 0
# creando jugador uno
jugadorA= turtle.Turtle()
jugadorA.speed(0) #esta velocidad es para que aparezca inmediatamente en la pantalla
jugadorA.shape("square")
jugadorA.color("blue")
jugadorA.penup()#para no dejar la linea
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)
#la pelota mide 20px   wid largo entonces multiplicamos 20 x 5 y el otro lo dejamosigual

#Creando jugador dos
jugadorB= turtle.Turtle()
# jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("red")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

# creando pelota

pelota= turtle.Turtle()
pelota.speed()
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx= 3 #separar las  x e y #esto es para mover la pelota es como en matemática cambiar x e y
pelota.dy = 3 #significa que la pelota se movera cada 3 pixeles


# division cancha
division= turtle.Turtle() # esto es para dibujar la línea
division.color("white")
division.goto(0, 400) #primero eje x
division.goto(0,-400)

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A : 0          Jugador B : 0", align= "center", font=("Courier", 24, "normal"))


# # funciones para mover jugadores
# obtener las coordenadas es como un plano cartesiano las y es para arriba y para abajo

def jugadorA_arriba():
    y= jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_abajo():
    y= jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_arriba():
    y= jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_abajo():
    y= jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)




# teclado
wn.listen()
wn.onkeypress(jugadorA_arriba, "w")
wn.onkeypress(jugadorA_abajo, "s")
wn.onkeypress(jugadorB_arriba, "Up")
wn.onkeypress(jugadorB_abajo, "Down")




while True:
    wn.update()
    pelota.setx(pelota.xcor() + pelota.dx) # se irá aumentando mi coordenada con lo que agregué arriba de los 3 pixeles
    pelota.sety(pelota.ycor() + pelota.dy)

    # bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1  #revertir es de 290 porque la pantalla es de 600  y la pelota es de 20 pxl

    if pelota.ycor() < -290:
        pelota.dy *= -1 #revertir

    #bordes derecha e izquierda

    if pelota.xcor() > 390: #el ancho de la pantalla
        pelota.goto(0,0) # si sale ,redimensionar la pelota
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("Jugador A : 0          Jugador B : 0".format(marcadorA, marcadorB), align= "center", font=("Courier", 24, "normal"))

    if pelota.xcor() <-390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB +=1
        pen.clear() #Para limpiar el marcador
        pen.write("Jugador A : {}          Jugador B : {}".format(marcadorA, marcadorB), align= "center", font=("Courier", 24, "normal"))

# Para trabajar en  las colisiones debe encontrarse entre el alto  y ancho de la paleta
    if ((pelota.xcor()> 340 and pelota.xcor()< 350)# si la coordenada de la paleta es mayor de 340 y menor de 350
            and(pelota.ycor()< jugadorB.ycor()+50 # menor que al jugador b le sumo 50
            and pelota.ycor()> jugadorB.ycor()-50)):# mayor a jugador b meno 50
        pelota.dx *= -1 # revierto la posicion

    if ((pelota.xcor()< -340 and pelota.xcor()> -350) #menor mayor
            and(pelota.ycor()< jugadorA.ycor()+ 50
            and pelota.ycor()> jugadorA.ycor()-50)):
        pelota.dx *= -1


# hay que revisar donde está ubicada la paleta