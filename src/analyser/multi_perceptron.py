
from perceptron import *

class multiNeuron:

    def __init__(self, nb_input_values : int, nb_input : int, hidden_list : list[int]) -> None:
        self.neural_network : list[list[Perceptron]] = []
        self.init_network(nb_input_values, nb_input, hidden_list)

    def init_network(self, nb_input_values : int, nb_input : int, hidden_list : list[int]) -> None:
        # First layer
        self.neural_network.append([Perceptron(nb_input_values)])
        for i in range(nb_input - 1):
            self.neural_network[0].append(Perceptron(nb_input_values))

        # Hidden layers
        nb_last_input : int = nb_input
        layer_iterator : int = 1
        for i in hidden_list:
            self.neural_network.append([Perceptron(nb_last_input)])
            for j in range(i - 1):
                self.neural_network[layer_iterator].append(Perceptron(nb_last_input))
            nb_last_input = i
            layer_iterator += 1

        # Output layer
        self.neural_network.append([Perceptron(nb_last_input)])

    def predict(self, input : list[int]) -> int:
        last_inputs : list[int] = []
        for layer in self.neural_network:
            last_inputs = []
            for neuron in layer:
                last_inputs.append(neuron.predict(input))
            input = last_inputs
        return input[0]

    def train(self, inputs : list[list[int]], targets : list[int], max_iteration=10000) -> None:
        for iteration in range(max_iteration):
            print("\r", iteration, end="")

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
