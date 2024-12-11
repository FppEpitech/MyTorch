import random
import sys
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def heaviside(x):
    return 1 if x >= 0 else 0

def heaviside_derivative(x):
    return 1

def relu(x):
    return max(0, x)

def relu_derivative(x):
    return 1 if x > 0 else 0

class Perceptron:
    def __init__(self, learning_rate : int, weights : list[int], bias : int, activation_function : str) -> None:
        self.weights = weights
        self.bias = bias
        self.learning_rate = learning_rate
        self.last_activation = 0
        self.last_inputs = []
        self.activation_function = None
        self.activation_derivative = None
        if (activation_function == "SIGMOID"):
            self.activation_function = sigmoid
            self.activation_derivative = sigmoid_derivative
        elif (activation_function == "HEAVYSIDE"):
            self.activation_function = heaviside
            self.activation_derivative = heaviside_derivative
        elif (activation_function == "RELU"):
            self.activation_function = relu
            self.activation_derivative = relu_derivative
        else:
            print(f"Error: Activation function not found : {activation_function}", file=sys.stderr)
            sys.exit(84)

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
