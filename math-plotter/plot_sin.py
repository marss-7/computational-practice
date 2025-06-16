import numpy as np
import matplotlib.pyplot as plt
import os

folder = os.path.dirname(__file__)

#We define the function to graph
def f1(x):
    """return the function sin(x) multiplied by x"""
    y = np.sin(x) * x
    return y

def f2(x):
    """return the function cos(x)"""
    y = np.cos(x)
    return y

#We ask the user for the function and xmin and xmax 
function = int(input("Write 1 for sin(x)*x and 2 for cos(x): "))
xmin = int(input("Write the lower limit for the function: "))
xmax = int(input("Write the upper limit for the function: "))

if xmin >= xmax:
    print("Lower limit must be less than upper limit.")
    exit()

if function == 1:
    function = f1
    label = "sin(x)*x"
elif function == 2:
    function = f2
    label = "cos(x)"
else:
    print("Invalid option.")
    exit()

X = np.linspace(xmin, xmax, 200)

#Now we plot:
plt.figure(figsize=(7,4))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(X, function(X), 'm-', label=label)
plt.title('Graph of the function ' + label)
plt.grid()
plt.legend()
plt.savefig(os.path.join(folder, 'function_plot.png'))
plt.show()