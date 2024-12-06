from Perceptron import Perceptron
import json

class Generator :

    def __init__(self, nb_input_values : int, nb_input : int, hidden_list : list[int]) -> None:
        self.neural_network : list[list[Perceptron]] = []
        self.nb_input_values : int = nb_input_values
        self.nb_layouts : int = len(hidden_list) + 1
        self.init_network(nb_input_values, nb_input, hidden_list)

    def init_network(self, nb_input_values : int, nb_input : int, hidden_list : list[int]) -> None:
        self.neural_network.append([Perceptron(nb_input_values)])
        for i in range(nb_input - 1):
            self.neural_network[0].append(Perceptron(nb_input_values))

        nb_last_input : int = nb_input
        layer_iterator : int = 1
        for i in hidden_list:
            self.neural_network.append([Perceptron(nb_last_input)])
            for j in range(i - 1):
                self.neural_network[layer_iterator].append(Perceptron(nb_last_input))
            nb_last_input = i
            layer_iterator += 1

        self.neural_network.append([Perceptron(nb_last_input)])

    def save_network(self, filepath : str = "neural_network.nn") -> None:
        network_data = {
            "nb_input_values": self.nb_input_values,
            "nb_layouts": self.nb_layouts,
            "layouts": [
                        [
                            json.loads(perceptron.save_state()) for perceptron in layout
                        ] for layout in self.neural_network
            ]
        }
        with open(filepath, "w") as file:
            json.dump(network_data, file, indent=4)
