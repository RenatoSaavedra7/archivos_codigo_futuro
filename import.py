import getpass

turtle.bgcolor("black")
pantalla=turtle.Turtle()
pantalla.pencolor("red")
pantalla.speed(20)

for i in range(400):
    pantalla.forward(i)
    pantalla.left(15)

turtle.mainloop()