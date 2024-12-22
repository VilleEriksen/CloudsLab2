from flask import Flask
from math import *

app = Flask(__name__)

@app.route('/calc/<lower>/<upper>')
def flask_intgabssin(lower, upper):
    lower = float(lower)
    upper = float(upper)
    
    n10 = calc(lower, upper, 10)
    n100 = calc(lower, upper, 100)
    n1000 = calc(lower, upper, 1000)
    n10k = calc(lower, upper, 10000)
    n100k = calc(lower, upper, 100000)
    n1m = calc(lower, upper, 1000000)
    
    return f"10: {n10} | 100: {n100} | 1000: {n1000} | 10k: {n10k} | 100k: {n100k} | 1m: {n1m}"
    

def calc(lower, upper, n):
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
