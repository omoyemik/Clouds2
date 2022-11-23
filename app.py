# clouds assignment 2 - Ex 1 --using Python, Flask
from flask import Flask
import numpy as np
import math

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Microservice Numerical Integration</p>"


@app.route("/integration/<lower>/<upper>")
def num_int(lower, upper):
    integral = numerical_integration(float(lower), float(upper))
    # print(integral)
    return f"<p>fResult for N = [10,100,1000,10000,100000, 1000000] is: {integral}</p>"


def numerical_integration(lower, upper):
    # defining function using lambda
    f = lambda x: abs(math.sin(x))

    f = np.vectorize(f)
    r = []

    for i in range(1, 7):
        N = 10 ** i  # use N = [10,100,1000,10000,100000, 1000000]

        x = np.linspace(lower, upper, N)

        dx = x[1] - x[0]

        y = f(x)

        r.append(np.sum(y * dx))

    return r


if __name__ == "__main__":
    app.run()
