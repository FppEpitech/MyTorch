#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## MyTorch
## File description:
## commandParsing
##

import sys

from enum import Enum

class Mode(Enum):
    PREDICT = "predict"
    TRAIN = "train"
    TRAIN_SAVE = "train_save"
    GENERATOR = "generator"

class CommandParsing:

    def __init__(self, command: list) -> None:
        self.parse(command)

    def parse(self, command: list) -> None:

        if (len(command) < 2):
            print("Binary should at least has one argument.")
            exit(84)

        binaries = {
            "./my_torch_analyzer": lambda command: self.parseAnalyzer(command),
            "./my_torch_generator": lambda command: self.parseGenerator(command)
        }

        if command[0] in binaries:
            try:
                binaries[command[0]](command)
            except (IndexError, ValueError):
                exit(84)
        else:
            exit(84)

    def parseAnalyzer(self, command: list) -> None:
        self.displayHelp(command)
        if (command[1] == "--predict" and len(command) == 4):
            return [Mode.PREDICT, command[2], command[3]]
        elif (command[1] == "--train" and len(command) == 4):
            return [Mode.TRAIN, command[2], command[3]]
        elif (command[1] == "--train" and len(command) == 6 and command[2] == "--save"):
            return [Mode.TRAIN_SAVE, command[2], command[3]]
        else:
            print("Error: Wrong parameters for ./my_torch_analyzer")
            exit(84)

    def parseGenerator(self, command: list) -> None:
        self.displayHelp(command)

    def displayHelp(self, command: list) -> None:
        if (command[1] != "--help"):
            return
        helps = {
            "./my_torch_analyzer": "USAGE\n"
            "\t./my_torch_analyzer [--predict | --train [--save SAVEFILE]] LOADFILE FILE\n\n"
            "DESCRIPTION\n"
            "\t--train Launch the neural network in training mode. Each chessboard in FILE must "
            "contain inputs to send to the neural network in FEN notation and the expected output "
            "separated by space. If specified, the newly trained neural network will be saved in "
            "SAVEFILE. Otherwise, it will be saved in the original LOADFILE.\n"
            "\t--predict Launch the neural network in prediction mode. Each chessboard in FILE "
            "must contain inputs to send to the neural network in FEN notation, and optionally an "
            "expected output.\n"
            "\t--save Save neural network into SAVEFILE. Only works in train mode.\n\n"
            "\tLOADFILE File containing an artificial neural network\n"
            "\tFILE File containing chessboards",

            "./my_torch_generator": "USAGE\n"
            "\t./my_torch_generator config_file_1 nb_1 [config_file_2 nb_2...]\n\n"
            "DESCRIPTION\n"
            "\tconfig_file_i Configuration file containing description of a neural network we want "
            "to generate.\n"
            "\tnb_i Number of neural networks to generate based on the configuration file."
        }

        if command[0] in helps:
            try:
                print(helps[command[0]])
                exit(0)
            except (IndexError, ValueError):
                print("Error with display --help")
                exit(84)
        else:
            print("Error with display --help")
            exit(84)
