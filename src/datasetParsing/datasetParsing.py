#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## MyTorch
## File description:
## datasetParsing
##

import string
import sys

mapTurnInt = {
    "w": -1,
    "b": 1
}

mapCharToIntPlate = {
    ".": 0,
    "p": 1,
    "r": 2,
    "n": 3,
    "b": 4,
    "k": 5,
    "q": 6
}

mapOutcomeInt = {
    # "Checkmate": 1,
    "Checkmate Black": 1,
    "Checkmate White": 2,
    "Stalemate": 3,
    "Nothing": 4,
    "Check White": 5,
    "Check Black": 6,
    # "Check": 5,
}

class chessSate():
    def __init__(self):
        self.chessPlate = []
        self.move: int = None
        self.turn : int = 0
        self.castlingrights : str = ""
        self.targetsquare = ''
        self.halfmoveclock : int= -1
        self.fullmove  : int = -1
    def __str__(self):
        return f"plate: {self.chessPlate} move: {self.move} turn: {self.turn} castlingrights: {self.castlingrights} targetsquare: {self.targetsquare} halfmoveclock: {self.halfmoveclock} fullmove: {self.fullmove}"

def parseFile(filePath: str) -> list[chessSate]:
    file = open(filePath, "r")
    if file is None:
        return None
    lines = file.readlines()
    file.close()
    ret : list[chessSate] = []
    for dataLine in lines:
        state = chessSate()
        parseDataLine(state, dataLine)
        ret.append(state)
    return ret

def parseDataLine(state : chessSate, line : str):
    line = line.replace('\n', '')
    parsed = line.split(" ")
    if len(parsed) < 6:
        print("LACKING ARGUMENTS IN DATASET")
        sys.exit(84)
    plateStrFen = parsed[0]
    state.turn = turnToInt(parsed[1])
    state.castlingrights = parsed[2]
    state.targetsquare = parsed[3]
    state.halfmoveclock = parsed[4]
    state.fullmove = parsed[5]
    if (len(parsed) > 6):
        tmp = parsed[6] + " " +  parsed[7]
        if (tmp not in mapOutcomeInt.keys()):
            print("INVALID MOVE IN DATASET")
            sys.exit(84)
        state.move = outcomeToInt(tmp)
    processFenStr(plateStrFen, state.chessPlate)

def processFenStr(line : str, plate):
    plateRows : list[str] = line.split("/")
    if len(plateRows) != 8:
        print("INVALID NUM ROWS IN DATASET")
        sys.exit(84)
    for row in plateRows:
        newRow : list[list] = []
        for char in row:
            if char not in "prnbkqPRNBKQ" and not char.isnumeric():
                print("INVALID CHAR FOUND IN DATASET")
                sys.exit(84)
            if char.isnumeric():
                    for i in range(int(char)):
                        newRow.append(charToIntChessplate('.'))
            else:
                newRow.append(charToIntChessplate(char))
        plate.append(newRow)

def charToIntChessplate(char : str) -> int:

    res : int = 0
    if (char in mapCharToIntPlate.keys()):
        res = mapCharToIntPlate[char.lower()]
    if (char.isupper()):
        res = -res
    return res

def turnToInt(turn : str) -> int:
    return mapTurnInt[turn]

def outcomeToInt(outcome : str) -> int:
    return mapOutcomeInt[outcome]

for i in parseFile("tests/datasets/check/10_pieces.txt"):
    print(i)
#robustness & perfectionne all - logic later
