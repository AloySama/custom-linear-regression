import numpy as np


class LinearModel:
    def __init__(self, learning_rate: float = 5e-3, epochs: int = 10):
        self.losses = None
        self.b = None
        self.W = None
        self.lr = learning_rate
        self.epochs = epochs
        self.wb_list = []

    def __initialisation__(self, X):
        W = np.random.randn(X.shape[1], 1)
        b = np.random.randn(1)
        return W, b

    def __model__(self, X, W, b):
        Z = X.dot(W) + b

        A = 1 / (1 + np.exp(-Z))

        return A

    def __log_loss__(self, A, y) -> float:
        m = len(y)

        return 1 / m * np.sum(-y * np.log(A) - (1 - y) * np.log(1 - A))

    def __descent_gradient__(self, A, X, y):
        m = len(y)
        dW = 1 / m * np.dot(X.T, A - y)

        db = 1 / m * np.sum(A - y)

        return dW, db

    def __update__(self, dW, db, W, b, learning_rate=1e-5):
        W = W - learning_rate * dW
        b = b - learning_rate * db

        return W, b

    def fit(self, X, y):
        W, b = self.__initialisation__(X)

        losses = []

        for i in range(self.epochs):
            A = self.__model__(X, W, b)
            loss = self.__log_loss__(A, y)
            losses.append(loss)

            dW, db = self.__descent_gradient__(A, X, y)

            W, b = self.__update__(dW, db, W, b, self.lr)
            if i % 10 == 0:
                self.wb_list.append(([W[0][0], W[1][0]], b[0]))

        self.W = W
        self.b = b
        self.losses = losses
        return W, b, losses

    def predict(self, X, threshold=.5):
        return self.__model__(X, self.W, self.b) >= threshold
