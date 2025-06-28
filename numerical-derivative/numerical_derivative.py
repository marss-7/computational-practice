import os
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

#we ccreate the function that turns the input into a workable function.
def f(s):
    P = sp.simplify(s)
    func = sp.lambdify(x, P, 'numpy')
    return func

def numderivative(f, xo, h):
    forward = (f(xo + h) - f(xo))/h
    central = (f(xo + h) - f(xo - h))/(2 * h)
    backward = (f(xo) - f(xo - h))/h
    ders = [forward, central, backward]
    print(f"The value for the forward derivative at the point {xo} is {forward}, for the central is {central} and for the backward is {backward}")
    return ders

def dergraph(xi, yi, der, xdata):
    labels = ["Forward", "Central", "Backward"]
    colors = ['r--', 'c--', 'g--']
    for df, label, color in zip(der, labels, colors):
        intercept = yi - df * xi
        y = df * xdata + intercept
        plt.plot(xdata, y, color, label=f'{label} derivative')

repeat = True
folder = os.path.dirname(__file__)
x = sp.symbols('x')

# Main program loop
while repeat == True:
    # Ask for input
    s = input("Enter a function of f(x): ")
    xo = float(input("Write the point xo at which you wish to calculate the derivative: "))
    h = float(input("Write the small step h for the derivative: "))
    xmin = xo - 1
    xmax = xo + 1
    try:
        #We make the data
        funct = f(s)
        ders = numderivative(funct, xo, h)
        xpoints = np.linspace(xmin, xmax, 200)
        yi = funct(xo)
        #Now we plot:
        plt.figure(figsize=(7,4))
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.plot(xpoints, funct(xpoints), 'm-', label=s)
        plt.plot(xo, yi, 'b.')
        dergraph(xo, yi, ders, xpoints)
        plt.title('Graph of the function ' + s)
        plt.grid()
        plt.legend()
        plt.savefig(os.path.join(folder, 'derivatives_plot'))
        plt.show()
        # Ask if the user wants to continue.
        rep = input("Do you want to continue? Press q to quit.  ")
        if rep.lower() == "q":
            repeat = False
    except Exception as e:
        print("Something went wrong with the function input. Try again.")
        continue