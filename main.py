import numpy as np
from math import exp
from sklearn.datasets import make_blobs




def sigmoid(Z: np.array):
    return 1 / (1 + exp(-Z))


def log_loss(y, A: np.array) -> float:
    m = A.shape[0]

    return -1/m * sum(y * np.log(A) + (1 - y) * np.log(1 - A))


def linear_function(X: np.array, W: np.array, b: float):
    return X + W + b


def descent_gradient(y: float, X: np.array, A: np.array):
    m = A.shape[0]
    dW = 1/m * X.T * (A - y)

    db = 1/m * sum(A - y)

    return dW, db


def update(W, b, dW, db):
    pass

def initialise(X: np.array):
    columns = X.shape[1]
    print(columns)
