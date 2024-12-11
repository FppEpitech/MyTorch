import json

from src.generator.PerceptronLite import PerceptronLite

class Generator :

    def __init__(self, nb_input_values : int, nb_layers : int, layers_nb_neurons : list[int], layers_activation_functions : list[str], learning_rate : int, nb_output_neurons : int) -> None:
        self.neural_network : list[list[PerceptronLite]] = []
        self.nb_input_values : int = nb_input_values
        self.nb_layouts : int = len(layers_nb_neurons) + 1
        self.learning_rate : int = learning_rate
        self.nb_output_neurons : int = nb_output_neurons
        self.init_network(nb_layers, layers_nb_neurons, layers_activation_functions)

    def init_network(self, nb_layers : int, layers_nb_neurons : list[int], layers_activation_functions : list[str]) -> None:

        nb_last_input : int = nb_layers
        layer_iterator : int = 0

        for i in range(len(layers_nb_neurons)):
            self.neural_network.append([PerceptronLite(nb_last_input, layers_activation_functions[i])])
            for _ in range(i - 1):
                self.neural_network[layer_iterator].append(PerceptronLite(nb_last_input, layers_activation_functions[i]))
            nb_last_input = i
            layer_iterator += 1

        self.neural_network.append([PerceptronLite(nb_last_input, 'HEAVYSIDE')])
        for _ in range(self.nb_output_neurons - 1):
            self.neural_network[layer_iterator].append(PerceptronLite(nb_last_input, 'HEAVYSIDE'))

    def save_network(self, filepath : str = "neural_network_1.nn") -> None:
        network_data = {
            "nb_input_values": self.nb_input_values,
            "nb_layouts": self.nb_layouts,
            "learning_rate": self.learning_rate,
            "nb_output_neurons": self.nb_output_neurons,
            "layouts": [
                        [
                            json.loads(perceptron.save_state()) for perceptron in layout
                        ] for layout in self.neural_network
            ]
        }
        with open(filepath, "w") as file:
            json.dump(network_data, file, indent=4)
