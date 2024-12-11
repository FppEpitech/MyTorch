#!/usr/bin/env python3

import sys
import math

from src.commandParsing.commandParsing import *
from src.analyzer.multi_perceptron import multiNeuron
from src.datasetParsing.datasetParsing import *

def display_result(outputs : list[int]) -> None:
    if (len(outputs) != 6):
        exit(0)
    max = -math.inf
    max_index = 0
    for index, value in enumerate(outputs):
        if max < value:
            max = value
            max_index = index
    for i in mapOutcomeList:
        if mapOutcomeList[i][max_index] == 1:
            print(i)


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
            outputs : list[int] = mlp.predict(input)
            display_result(outputs)

    else:
        print("train")

if __name__ == "__main__":
    main()
