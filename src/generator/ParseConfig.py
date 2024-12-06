class ParseConfFile:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.nb_inputs = 0
        self.nb_layouts = 0
        self.neurons_per_layer = []

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
                    elif key == "nb_layouts":
                        self.nb_layouts = int(value)
                        self.neurons_per_layer = [0] * self.nb_layouts
                    elif key.startswith("nb_neuron_layout_"):
                        layout_index = int(key.split("_")[-1]) - 1
                        if (layout_index < self.nb_layouts) :
                            self.neurons_per_layer[layout_index] = int(value)

        except FileNotFoundError:
            print(f"Le fichier de configuration '{self.config_file}' n'existe pas.")
        except Exception as e:
            print(f"Erreur lors du parsing : {e}")

    def get_config(self):
        return {
            "nb_inputs": self.nb_inputs,
            "nb_layouts": self.nb_layouts,
            "neurons_per_layer": self.neurons_per_layer
        }
