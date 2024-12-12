import random
import json

class PerceptronLite:
    def __init__(self, nb_inputs, activation_function) -> None:
        self.weights : list[int] = [random.uniform(-1, 1) for _ in range(nb_inputs)]
        self.bias : int = random.uniform(-1, 1)
        self.activation_function : str = activation_function

    def save_state(self) -> str:
        state = {
            "weights": self.weights,
            "bias": self.bias,
            "activation_function": self.activation_function
        }
        return json.dumps(state)
