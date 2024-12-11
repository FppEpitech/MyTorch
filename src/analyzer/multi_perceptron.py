from src.analyzer.perceptron import *
from src.datasetParsing.datasetParsing import chessState

import json

class multiNeuron:

    def __init__(self, loading_file: str) -> None:
        self.neural_network : list[list[Perceptron]] = []
        self.init_network(loading_file)

    def init_network(self, loading_file: str) -> None:
        with open(loading_file, "r") as file:
            json_data = json.load(file)

        learning_rate : int = json_data["learning_rate"]
        layouts : list[list[dict]] = json_data["layouts"]

        index : int = 0
        for layout in layouts:
            weights : list[int] = layout[0]["weights"]
            bias : int = layout[0]["bias"]
            self.neural_network.append([Perceptron(learning_rate, weights, bias)])
            for i in range(len(layout) - 1):
                weights = layout[i]["weights"]
                bias = layout[i]["bias"]
                self.neural_network[index].append(Perceptron(learning_rate, layout[i]["weights"], layout[i]["bias"]))
            index += 1

    def predict(self, input : chessState) -> list[int]:
        last_inputs : list[int] = []
        for layer in self.neural_network:
            last_inputs = []
            for neuron in layer:
                last_inputs.append(neuron.predict(input))
            input = last_inputs
        return input

    def train(self, inputs : list[list[int]], targets : list[int], max_iteration=10000) -> None:
        for iteration in range(max_iteration):
            for i in range(len(targets)):
                prediction : int = self.predict(inputs[i])
                if (prediction != targets[i]):
                    self.update_parameters(prediction, targets[i])

    def update_parameters(self, prediction: int, target: int) -> None:
        quadratic_error: float = target - prediction
        output_delta: float = quadratic_error * sigmoid_derivative(prediction)

        output_layer = self.neural_network[-1]
        deltas: list[float] = []
        for neuron in output_layer:
            for weight_index in range(len(neuron.weights)):
                neuron.weights[weight_index] += neuron.learning_rate * output_delta * neuron.last_inputs[weight_index]
            neuron.bias += neuron.learning_rate * output_delta
            deltas.append(output_delta)

        for layer_index in range(len(self.neural_network) - 2, -1, -1):
            current_layer = self.neural_network[layer_index]
            next_layer = self.neural_network[layer_index + 1]
            next_deltas = deltas

            new_deltas: list[float] = []
            for neuron_index, neuron in enumerate(current_layer):
                error = sum(
                    next_neuron.weights[neuron_index] * next_deltas[next_neuron_index]
                    for next_neuron_index, next_neuron in enumerate(next_layer)
                )
                delta = error * sigmoid_derivative(neuron.last_activation)
                new_deltas.append(delta)
                for weight_index in range(len(neuron.weights)):
                    neuron.weights[weight_index] += neuron.learning_rate * delta * neuron.last_inputs[weight_index]
                neuron.bias += neuron.learning_rate * delta
            deltas = new_deltas

    def save(self):
        pass
