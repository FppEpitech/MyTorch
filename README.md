
# My_Torch: A Clash of Kings

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How to Use](#how-to-use)
- [Usage](#usage)
  - [Neural Network Generator](#neural-network-generator)
  - [Chessboard Analyzer](#chessboard-analyzer)
- [Compilation](#compilation)

---

## Introduction

My_Torch is a strategy-based machine-learning project inspired by the world of chess. It provides tools to generate neural networks and analyze chessboard states, paving the way for strategic supremacy. This project eschews external machine learning libraries (e.g., PyTorch, TensorFlow) in favor of custom implementations, emphasizing controlled training and robust prediction capabilities.

---

## Features

1. **Neural Network Generator**
   Create customizable neural networks from configuration files for tailored strategies.

2. **Chessboard Analyzer**
   Analyze chessboard states using the Forsyth–Edwards Notation (FEN) in:
   - **Training mode**: Train networks with supervised learning.
   - **Prediction mode**: Classify board states into "Checkmate", "Check", "Stalemate", or "Nothing".

---

## How to Use

### 1. Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/username/my_torch.git
cd my_torch
```

### 2. Build the Project
Use the provided `Makefile` to build the binaries:
```bash
make
```

This will generate the binaries:
- `my_torch_generator`
- `my_torch_analyzer`

See how to use them in the [Usage](#usage) section.

---

## Usage

### Neural Network Generator

Command format:
```bash
./my_torch_generator config_file_1 nb_1 [config_file_2 nb_2...]
```

- **Parameters**:
  - `config_file_i`: File specifying the neural network configuration.
  - `nb_i`: Number of neural networks to generate.

- **Example**:
  ```bash
  ./my_torch_generator basic_network.conf 3
  ```

  Outputs:  
  `basic_network_1.nn`, `basic_network_2.nn`, `basic_network_3.nn`.

### Chessboard Analyzer

Command format:
```bash
./my_torch_analyzer [--predict | --train [--save SAVEFILE]] LOADFILE FILE
```

- **Parameters**:
  - `--train`: Trains the network using FEN inputs and expected outputs.
  - `--predict`: Predicts states for chessboards in the input file.
  - `--save`: (Optional) Specifies a file to save the trained network.

- **Example**:
  ```bash
  ./my_torch_analyzer --predict my_torch_network.nn chessboards.txt
  ```

---

## Compilation

The project includes a Makefile with the following rules:
- `make`: Builds the project.
- `make clean`: Removes object files.
- `make fclean`: Removes binaries and temporary files.
- `make re`: Cleans and rebuilds the project.
