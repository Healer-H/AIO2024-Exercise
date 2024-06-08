import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def elu(x, alpha=1):
    if x <= 0:
        return alpha * (np.exp(x) - 1)
    else:
        return x
    
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def calculate_activation_function():
    x = input('Input x = ')
    if not is_number(x):
        print('x must be a number')
        return None
    
    activation_function = input('Input activation function (sigmoid, relu, elu) = ')
    if activation_function not in ['sigmoid', 'relu', 'elu']:
        print(f"{activation_function} is not suppotred. \nPlease choose one of these: sigmoid, relu, elu")
        return None
    
    if activation_function == 'sigmoid':
        print(f"sigmoid({x}) = {sigmoid(float(x))}")
        
    elif activation_function == 'relu':
        print(f"relu({x}) = {relu(float(x))}")
        
    else: 
        print(f"elu({x}) = {elu(float(x))}")
    
if __name__ == '__main__':
    calculate_activation_function()