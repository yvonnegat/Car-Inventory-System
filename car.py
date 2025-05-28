import turtle as t
import random
import flowers as rose
import truck as truck
import suv as sv
import vehicle as v
import tkinter as tk


def rand_colors():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


def drawCar():
    t.hideturtle()
    t.speed(0)
    a = 0.5
    b = 1.5
    u = random.random()
    size_factor = a + (u * (b - a))

    # Car body
    t.penup()
    t.goto(-200 * size_factor, -50 * size_factor)
    t.pendown()
    t.fillcolor(rand_colors())
    t.begin_fill()
    for _ in range(2):
        t.forward(400 * size_factor)
        t.left(90)
        t.forward(50 * size_factor)
        t.left(90)
    t.end_fill()
    t.penup()

    # Outer trapezium
    t.goto(-150 * size_factor, 0)
    t.setheading(0)
    t.fillcolor(rand_colors())
    t.begin_fill()
    t.pendown()
    t.left(40)
    t.forward(80 * size_factor)
    t.setheading(0)
    t.forward(150 * size_factor)
    t.right(40)
    t.forward(80 * size_factor)
    t.end_fill()

    # Left inner trapezium
    t.fillcolor("grey")
    t.begin_fill()
    t.penup()
    t.goto(-130 * size_factor, 5 * size_factor)
    t.setheading(0)
    t.pendown()
    t.left(40)
    t.forward(60 * size_factor)
    t.setheading(0)
    t.forward(70 * size_factor)
    t.right(90)
    t.forward(40 * size_factor)
    t.right(90)
    t.forward(117 * size_factor)
    t.end_fill()

    # Right inner trapezium
    t.penup()
    t.backward(117 * size_factor)
    t.left(90)
    t.backward(40 * size_factor)
    t.setheading(0)
    t.forward(10 * size_factor)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.forward(60 * size_factor)
    t.right(40)
    t.forward(61 * size_factor)
    t.setheading(180)
    t.forward(108 * size_factor)
    t.right(90)
    t.forward(41 * size_factor)
    t.end_fill()

    # Back tire
    t.penup()
    t.goto(-120 * size_factor, -75 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(25 * size_factor)
    t.end_fill()

    t.penup()
    t.goto(-120 * size_factor, -65 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.circle(15 * size_factor)
    t.end_fill()

    # Front tire
    t.penup()
    t.goto(120 * size_factor, -75 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(25 * size_factor)
    t.end_fill()

    t.penup()
    t.goto(120 * size_factor, -65 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.circle(15 * size_factor)
    t.end_fill()


def open_suv():
    t.title("Simulation and Modeling")
    t.clearscreen()
    sv.main()


def open_truck():
    t.title("Simulation and Modeling")
    t.clearscreen()
    truck.main()


def open_car():
    t.title("Simulation and Modeling")
    t.clearscreen()
    rose.main()
    main()


def main():
    t.setup(width=1280, height=650, startx=0, starty=0)
    screen = t.Screen()
    screen.bgcolor("white")

    drawCar()

    canvas = screen.getcanvas()

    # Styled buttons
    button_font = ("Helvetica", 10, "bold")
    Car_button = tk.Button(canvas.master, text="CAR", font=button_font, bg="#a8dadc", command=open_car)
    Suv_button = tk.Button(canvas.master, text="SUV", font=button_font, bg="#a8dadc", command=open_suv)
    Truck_button = tk.Button(canvas.master, text="TRUCK", font=button_font, bg="#a8dadc", command=open_truck)

    # Button positions
    Car_button.place(x=20, y=10, width=60, height=30)
    Suv_button.place(x=90, y=10, width=60, height=30)
    Truck_button.place(x=160, y=10, width=60, height=30)

    # Car object
    car = v.Car('BMW', 2001, 70000, 15000.0, 4)
    boldfont = ("Arial", 14, "bold")
    regfont = ("Cambri", 12, "normal")

    # Inventory text shifted down
    t.penup()
    t.goto(-100, 120)
    t.right(90)
    t.write("USED CAR INVENTORY", font=boldfont)

    t.goto(-200, 110)
    t.write("===========================================================================")

    t.goto(-200, 90)
    t.write('Make', font=boldfont)
    t.goto(-200, 70)
    t.write(f'{car.get_make()}', font=regfont)

    t.goto(-130, 90)
    t.write('Model', font=boldfont)
    t.goto(-130, 70)
    t.write(f'{car.get_model()}', font=regfont)

    t.goto(-60, 90)
    t.write('Mileage', font=boldfont)
    t.goto(-60, 70)
    t.write(f'{car.get_mileage()}', font=regfont)

    t.goto(20, 90)
    t.write('Price', font=boldfont)
    t.goto(20, 70)
    t.write(f'{car.get_price()}', font=regfont)

    t.goto(90, 90)
    t.write('Number of doors:', font=boldfont)
    t.goto(150, 70)
    t.write(f'{car.get_doors()}', font=regfont)

    t.done()


main()















































































