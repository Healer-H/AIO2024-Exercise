import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def approx_sin(x, n):
    approx = 0
    for i in range(n):
        approx += (-1) ** i * x ** (2 * i + 1) / factorial(2 * i + 1) 
    return approx
    
def approx_cos(x, n):
    approx = 0
    for i in range(n):
        approx += (-1) ** i * x ** (2 * i) / factorial(2 * i) 
    return approx

def approx_sinh(x, n):
    approx = 0
    for i in range(n):
        approx += x ** (2 * i + 1) / factorial(2 * i + 1) 
    return approx

def approx_cosh(x, n):
    approx = 0
    for i in range(n):
        approx += x ** (2 * i) / factorial(2 * i) 
    return approx

if __name__ == "__main__":
    x = float(input("Input x (float) = "))
    if x > 2 * math.pi:
        x = x % (2 * math.pi)
    n = int(input("Input n (integer) = ")) 
    print(f"sin({x}) = {math.sin(x)}")
    print(f"approx_sin({x}, {n}) = {approx_sin(x, n)}")
    print(f"cos({x}) = {math.cos(x)}")
    print(f"approx_cos({x}, {n}) = {approx_cos(x, n)}")
    print(f"sinh({x}) = {math.sinh(x)}")
    print(f"approx_sinh({x}, {n}) = {approx_sinh(x, n)}")
    print(f"cosh({x}) = {math.cosh(x)}")
    print(f"approx_cosh({x}, {n}) = {approx_cosh(x, n)}")