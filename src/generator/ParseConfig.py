class ParseConfFile:
    def __init__(self, config_file: str):
        self.config_file : str = config_file
        self.nb_inputs : int = 0
        self.nb_layers : int = 0
        self.nb_output_neurons : int = 0
        self.learning_rate : float = 0.0
        self.neurons_per_layer : list[int] = []
        self.activation_functions : list[str] = []

    def parse(self):
        try:
            with open(self.config_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue

                    key, value = line.split("=")
                    key, value = key.strip(), value.strip()

                    if key == "nb_inputs":
                        self.nb_inputs = int(value)
                    elif key == "nb_layers":
                        self.nb_layers = int(value)
                        self.neurons_per_layer = [0] * self.nb_layers
                        self.activation_functions = [""] * self.nb_layers
                    elif key == "learning_rate" :
                        self.learning_rate = float(value)
                    elif key == "nb_output_neurons":
                        self.nb_output_neurons = int(value)
                    elif key.startswith("nb_neuron_layout_"):
                        layout_index = int(key.split("_")[-1]) - 1
                        if layout_index < self.nb_layers:
                            values = value.split(",")
                            neuron_count = int(values[0].strip())
                            activation_function = values[1].strip() if len(values) > 1 else None

                            self.neurons_per_layer[layout_index] = neuron_count
                            if activation_function:
                                self.activation_functions[layout_index] = activation_function

        except FileNotFoundError:
            print(f"Le fichier de configuration '{self.config_file}' n'existe pas.")
        except Exception as e:
            print(f"Erreur lors du parsing : {e}")

    def get_config(self):
        return {
            "nb_inputs": self.nb_inputs,
            "nb_layers": self.nb_layers,
            "nb_output_neurons": self.nb_output_neurons,
            "learning_rate": self.learning_rate,
            "neurons_per_layer": self.neurons_per_layer,
            "activation_functions": self.activation_functions
        }
