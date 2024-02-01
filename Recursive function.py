def f(n):
    if n <=2:
        result = n
    else:
        result = f(n-2) + f(n-3)
    return result

s=input("Ingrese el numero que quiere ver ")
print(f(int(s)))


#Quiero declarar una variable que multiplique por 2 la función.

Multi=f(int(s))*2
print(Multi)

import turtle

def dibujar_petalos():
    for _ in range(36):
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(100)
        turtle.right(135)
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(100)
        turtle.right(135)

def dibujar_flor():
    turtle.fillcolor("red")
    turtle.begin_fill()
    dibujar_petalos()
    turtle.end_fill()

def dibujar_tallo():
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(20)
    turtle.end_fill()

def dibujar_pistilo():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

def main():
    turtle.speed(2)
    turtle.bgcolor("lightblue")

    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    dibujar_flor()

    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    dibujar_tallo()

    dibujar_pistilo()

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
