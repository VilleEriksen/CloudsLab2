from flask import Flask
from math import *

app = Flask(__name__)

@app.route('/calc/<lower>/<upper>/<n>')
def flask_intgabssin(lower, upper, n):
    lower = float(lower)
    upper = float(upper)
    n = int(n)
    
    sum = 0.0
    h = (upper - lower) / n
    
    for i in range(n):
        x = lower + (i * h)
        
        y = abs(sin(x))
        sum += h * y
    
    return f"{sum:.5f}"
