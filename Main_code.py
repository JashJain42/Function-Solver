import math
import matplotlib.pyplot as plt
import numpy as np

quad = 0
linear = 2
cubic = 3
expon = 1
exit=0

while exit == 0:
    wfunc = input("for quad enter 0, for expon enter 1, for linear enter 2, for cubic enter 3 or to exit enter 4")
    if wfunc == ("0"):
        a = int(input("a"))
        b = int(input("b"))
        c = int(input("c"))
        q = b ** 2
        print("square of b is", q)
        w = 4 * a * c
        qw = q - w
        print("4ac is", w)
        print("discriminant is", qw)
        r = (math.sqrt(qw))
        print("root of disc is", r)
        t = -b + r
        print("top part of formula is", t)
        y = 2 * a
        u = t / y
        print("the positive part of the disc is", u)
        g = -b - r
        j = g / y
        print("the negative part of the disc is", j)
        print("therefore the x intercepts are", j, u)
        x_vert = -b / 2 * a
        y_vert = a * (x_vert ** 2) + b * x_vert + c
        vertex = (x_vert, y_vert)
        print("the x intercepts are", u, "and", j, "the vertex is", vertex, "the y int is", c)
        x_cords = range(-1000, 1000)
        y_cords = [a * x * x + b * x + c for x in x_cords]
        plt.plot(x_cords, y_cords)
        plt.show()
    elif wfunc == ("2"):

        print("To plot linear equations please give the m(the gradient) and the c(y intercept) of the equation")
        gradient = int(input("the gradient: "))
        yint = int(input("the y intercept please: "))
        x_cords = range(-5, 5)
        y_cords = [gradient * x + yint for x in x_cords]
        plt.plot(x_cords, y_cords)
        plt.show()
    elif wfunc == ("3"):

        print("Let's plot a cubic function!")
        a_c = int(input("the a"))
        b_c = int(input("the b"))
        c_c = int(input("the c"))
        d_c = int(input("the d"))
        xcords = range(-50, 50)
        ycords = [a_c * x ** 3 + b_c * x ** 2 + c_c * x + d_c for x in xcords]
        plt.plot(xcords, ycords)
        plt.show()
    elif wfunc == ("1"):
        print("Let's plot exponential functions")
        a = int(input("a value: "))
        b = int(input("b value: "))
        h = int(input("h value: "))
        k = int(input("k value: "))
        xco = range(-10, 10)
        yco = [a * b ** (x + h) + k for x in xco]
        plt.plot(xco, yco)
        plt.show()
    elif wfunc == ("4"):
        exit = 1
    else:
        print("error!!!!")



