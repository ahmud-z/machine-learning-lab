import numpy as np

def sigmoid_func(z):
    return 1 / (1 + np.exp(-z))


class Logistic_Regression_Scratch:
    def __init__(self, lr=0.001, iterations=1000):
        self.lr = lr
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        no_samples, no_features = X.shape
        self.weights = np.zeros(no_features)
        self.bias = 0

        # GD
        for i in range(self.iterations):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = sigmoid_func(linear_model)

            # calculatr grads
            dw = (1 / no_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / no_samples) * np.sum(y_predicted - y)

            # update weights
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = sigmoid_func(linear_model)
        class_pred = [1 if i > 0.5 else 0 for i in y_predicted]
        return class_pred

    def accuracy(self, y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy
