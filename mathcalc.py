import math

f = lambda x: 3 * x**3 - 4 * x + 9

from mathcalc import f
if f is None:
    print("The function f(x) is not defined.")
else:
    xs = [x / 10.0 for x in range(-50, 51)]
    ys = [f(x) for x in xs]

    import matplotlib.pyplot as plt

    plt.plot(xs, ys)
    plt.title("Plot of f(x) = 3x^3 - 4x + 9")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

print("The function f(x) = 3x^3 - 4x + 9 has been plotted.")