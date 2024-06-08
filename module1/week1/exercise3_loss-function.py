import numpy as np
import math
import random

def mae(y_true, y_pred):
    n_samples = len(y_true)
    total_loss = 0
    for idx in range(n_samples):
        loss = np.abs(y_true[idx] - y_pred[idx])
        print(f"loss name: mae, sample: {idx}, pred: {y_pred[idx]}, target: {y_true[idx]}, loss: {loss}")
        total_loss += loss
    return 1 / n_samples * total_loss

def mse(y_true, y_pred):
    n_samples = len(y_true)
    total_loss = 0
    for idx in range(n_samples):
        loss = (y_true[idx] - y_pred[idx]) ** 2
        print(f"loss name: mse, sample: {idx}, pred: {y_pred[idx]}, target: {y_true[idx]}, loss: {loss}")
        total_loss += loss
    return 1 / n_samples * total_loss

def rmse(y_true, y_pred):
    n_samples = len(y_true)
    total_loss_sqr = 0
    for idx in range(n_samples):
        loss = (y_true[idx] - y_pred[idx]) ** 2
        print(f"loss name: rmse, sample: {idx}, pred: {y_pred[idx]}, target: {y_true[idx]}, loss: {loss}")
        total_loss_sqr += loss
    return math.sqrt(1 / n_samples * total_loss_sqr)

def calculate_loss_function():
    n_samples = input("Input n_samples = ")
    
    if n_samples.isnumeric() == False:
        print("number of samples must be an integer number")
        return None
    else: 
        n_samples = int(n_samples)
    
    loss_name = input("Input loss_name (mae, mse, rmse): ")
    if loss_name not in ["mae", "mse", "rmse"]:
        print("loss_name must be either mae, mse, or rmse")
        return None
    
    y_true = np.array([random.uniform(0, 10) for _ in range(n_samples)])
    y_pred = np.array([random.uniform(0, 10) for _ in range(n_samples)])
    
    if loss_name == "mae":
        loss = mae(y_true, y_pred)
        print(f"loss: {loss}")
    elif loss_name == "mse":
        loss = mse(y_true, y_pred)
        print(f"loss: {loss}")
    elif loss_name == "rmse":
        loss = rmse(y_true, y_pred)
        print(f"loss: {loss}")

if __name__ == "__main__":
    calculate_loss_function()