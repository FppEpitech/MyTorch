from src.generator.PerceptronLite import PerceptronLite
import json

class Generator :

    def __init__(self, nb_input_values : int, nb_layers : int, layers_content : list[int]) -> None:
        self.neural_network : list[list[PerceptronLite]] = []
        self.nb_input_values : int = nb_input_values
        self.nb_layouts : int = len(layers_content) + 1
        self.init_network(nb_input_values, nb_layers, layers_content)

    def init_network(self, nb_input_values : int, nb_layers : int, layers_content : list[int]) -> None:

        nb_last_input : int = nb_layers
        layer_iterator : int = 0

        for i in layers_content:
            self.neural_network.append([PerceptronLite(nb_last_input)])
            for _ in range(i - 1):
                self.neural_network[layer_iterator].append(PerceptronLite(nb_last_input))
            nb_last_input = i
            layer_iterator += 1

        self.neural_network.append([PerceptronLite(nb_last_input)])

    def save_network(self, filepath : str = "neural_network_1.nn") -> None:
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
