import random
import sys
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class Perceptron:
    def __init__(self, nb_inputs, learning_rate=0.01) -> None:
        self.weights = [random.uniform(-1, 1) for _ in range(nb_inputs)]
        self.bias = random.uniform(-1, 1)
        self.learning_rate = learning_rate
        self.activation_function = sigmoid
        self.last_activation = 0
        self.last_inputs = []

    def predict(self, inputs):
        if (len(inputs) != len(self.weights)):
            print("Error: Number of inputs must be the same as weight", file=sys.stderr)
            sys.exit(84)
        sum_prediction = 0
        self.last_inputs = inputs
        for i in range(len(inputs)):
            sum_prediction += inputs[i] * self.weights[i]
        sum_prediction += self.bias
        self.last_activation = self.activation_function(sum_prediction)
        return self.last_activation
