import logging
import azure.functions as func
import math
import numpy as np


def numerical_integration(lower, upper) :
    
    #defining function using lambda
    f = lambda x : abs(math.sin(x))

    f = np.vectorize(f)
    r = []

    for i in range(1,7):

        N = 10**i #use N = [10,100,1000,10000,100000, 1000000]

        x = np.linspace(lower,upper,N)

        dx = x[1] - x[0]

        y = f(x)

        r.append(np.sum(y * dx))
    
    return r


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('HTTP trigger function processed a request')

    lower = req.params.get('lower')    
    upper = req.params.get('upper')    
    
    if lower and upper:

        integral = numerical_integration(float(lower),float(upper))
        return func.HttpResponse(f"The result for N = [10,100,1000,10000,100000, 1000000] is: {integral}")
   
    else:
        return func.HttpResponse(
             "Missing argument. Please provide lower and upper bounds.",
             status_code=200
        )