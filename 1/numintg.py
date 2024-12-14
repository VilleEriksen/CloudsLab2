from math import *

def intgabssin(lower, upper, n):
    sum = 0.0
    h = (upper - lower) / n
    
    for i in range(n):
        x = lower + (i * h)
        
        y = abs(sin(x))
        sum += h * y
    
    return sum
        
if __name__ == "__main__":
    while True:
        try:
            lower = float(input("Lower: "))
            upper = float(input("Upper: "))
            n = int(input("Intervals: "))
            
            result = intgcossin(lower, upper, n)
            print(f"{result:.5f}")
        except ValueError:
            print("ValueError")