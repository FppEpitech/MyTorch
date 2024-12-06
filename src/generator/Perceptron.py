import random
import json
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

    def save_state(self, filename="perceptron_state.json") -> str:
        state = {
            "weights": self.weights,
            "bias": self.bias,
            "learning_rate": self.learning_rate
        }
        return json.dumps(state)

    def update_weights(self, inputs, target):
        prediction = self.predict(inputs)
        error = target - prediction

        self.weights = [
            self.weights[i] + self.learning_rate * error * inputs[i]
            for i in range(len(inputs))
        ]
        self.bias += self.learning_rate * error

    def predict(self, inputs):
        if (len(inputs) != len(self.weights)):
            print("Error: Number of inputs must be the same as weight", file=sys.stderr)
            sys.exit(84)
        sum_prediction = 0
        for i in range(len(inputs)):
            sum_prediction += inputs[i] * self.weights[i]
        sum_prediction += self.bias
        return self.activation_function(sum_prediction)

def train_perceptron(perceptron, training_data : list[tuple[list[int], int]], max_iterations=100000):
    for _ in range(max_iterations):
        all_correct = True

        for inputs, target in training_data:
            if perceptron.predict(inputs) != target:
                all_correct = False
                break
        if all_correct:
            return

        inputs, target = random.choice(training_data)
        perceptron.update_weights(inputs, target)

