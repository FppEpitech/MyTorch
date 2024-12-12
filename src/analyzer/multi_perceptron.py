import copy
from src.analyzer.perceptron import *
from src.datasetParsing.datasetParsing import chessState

import json

class multiNeuron:

    def __init__(self, loading_file: str) -> None:
        self.neural_network : list[list[Perceptron]] = []
        self.learning_rate : int = 0
        self.init_network(loading_file)

    def init_network(self, loading_file: str) -> None:
        with open(loading_file, "r") as file:
            json_data = json.load(file)

        learning_rate : int = json_data["learning_rate"]
        layouts : list[list[dict]] = json_data["layouts"]

        self.learning_rate = learning_rate

        index : int = 0
        for layout in layouts:
            weights : list[int] = layout[0]["weights"]
            bias : int = layout[0]["bias"]
            activation_function : str = layout[0]["activation_function"]
            self.neural_network.append([Perceptron(learning_rate, weights, bias, activation_function)])
            for i in range(len(layout) - 1):
                weights = layout[i]["weights"]
                bias = layout[i]["bias"]
                activation_function = layout[0]["activation_function"]
                self.neural_network[index].append(Perceptron(learning_rate, weights, bias, activation_function))
            index += 1

    def predict(self, input : list) -> list[int]:
        last_inputs : list[int] = []
        for layer in self.neural_network:
            last_inputs = []
            for neuron in layer:
                last_inputs.append(neuron.predict(input))
            input = last_inputs

        if last_inputs == []:
            return []
        max_value = max(last_inputs)
        max_index = last_inputs.index(max_value)
        result = [1 if i == max_index else 0 for i in range(len(last_inputs))]
        return result

    def train(self, inputs : list[list], targets : list[int], max_iteration=10000) -> None:

        total : int = 0
        total_good : int = 0

        for iteration in range(max_iteration):
            for i in range(len(targets)):
                prediction : int = self.predict(inputs[i])
                total += 1
                if (prediction != targets[i]):
                    print(f"\033[31m{iteration}: {prediction} - {targets[i]}\033[0m")
                    self.update_parameters(prediction, targets[i])
                else:
                    total_good += 1
                    print(f"\033[32m{iteration}: {prediction} - {targets[i]}\033[0m")
        print("============================")
        if (total != 0):
            print(f"result : {100 * total_good / total}%")
        else:
            print(f"result : 0 tests trained.")

    def update_parameters(self, prediction: int, target: int) -> None:

        if len(prediction) != 6:
            print("Error: length of prediction output not equal to 6.")
            exit(84)

        output_layer = self.neural_network[-1]
        deltas: list[float] = []
        for i, neuron in enumerate(output_layer):
            quadratic_error: float = target[i] - prediction[i]
            output_delta: float = quadratic_error * sigmoid_derivative(prediction[i])
            if (output_delta > 0):
                print("OUTPUT DELTA BORDEL FJKDQLMFJDKLQFMJD")
            keepweights = neuron.weights.copy()
            for weight_index in range(len(neuron.weights)):
                neuron.weights[weight_index] += neuron.learning_rate * output_delta * neuron.last_inputs[weight_index]
            if (neuron.weights != keepweights):
                print("WEIGHTS UPDATED BORDEL FJKDQLMFJDKLQFMJD")
            keep = neuron.bias
            neuron.bias += neuron.learning_rate * output_delta
            if (neuron.bias != keep):
                print("BIAS UPDATED BORDEL FJKDQLMFJDKLQFMJD")
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
                keepweights = neuron.weights.copy()
                for weight_index in range(len(neuron.weights)):
                    neuron.weights[weight_index] += neuron.learning_rate * delta * neuron.last_inputs[weight_index]
                if (neuron.weights != keepweights):
                    print("WEIGHTS UPDATED BORDEL FJKDQLMFJDKLQFMJD")
                keep = neuron.bias
                neuron.bias += neuron.learning_rate * delta
                if (neuron.bias != keep):
                    print("BIAS UPDATED BORDEL FJKDQLMFJDKLQFMJD")
            deltas = new_deltas

    def save_network(self, filepath : str = "neural_network_1.nn") -> None:
        network_data = {
            "learning_rate": self.learning_rate,
            "layouts": [
                        [
                            json.loads(perceptron.save_state()) for perceptron in layout
                        ] for layout in self.neural_network
            ]
        }
        with open(filepath, "w") as file:
            json.dump(network_data, file, indent=4)
