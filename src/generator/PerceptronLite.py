import random
import json

class PerceptronLite:
    def __init__(self, nb_inputs, learning_rate=0.01) -> None:
        self.weights = [random.uniform(-1, 1) for _ in range(nb_inputs)]
        self.bias = random.uniform(-1, 1)
        self.learning_rate = learning_rate

    def save_state(self, filename="perceptron_state.json") -> str:
        state = {
            "weights": self.weights,
            "bias": self.bias,
            "learning_rate": self.learning_rate
        }
        return json.dumps(state)
