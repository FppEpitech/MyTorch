#!/usr/bin/env python3

import sys

from src.commandParsing.commandParsing import *
from src.analyzer.multi_perceptron import multiNeuron
from src.datasetParsing.datasetParsing import *

def main():
    parser : CommandParsing = CommandParsing()
    command : list = parser.parse(sys.argv)

    if command[0] == Mode.PREDICT:
        mlp = multiNeuron(command[1])
        chessParsing = parseFile(command[2])
        for board_state in chessParsing:
            board : list[int] = [y for x in board_state.chessPlate for y in x]
            outcome : list[int] = [i for i in board_state.outcome]
            input = board + outcome + [board_state.turn, board_state.castlingrights, board_state.targetsquare, board_state.halfmoveclock, board_state.fullmove]
            mlp.predict(input)
    else:
        print("train")

if __name__ == "__main__":
    main()
