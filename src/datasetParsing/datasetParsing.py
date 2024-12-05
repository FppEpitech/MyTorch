#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## MyTorch
## File description:
## datasetParsing
##

import string
import sys

class chessSate():
    def __init__(self):
        self.chessPlate = []
        self.move: tuple[int, int] = (-1, -1)
        self.turn : str = ''
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
    plateStrFen = parsed[0]
    state.turn = parsed[1]
    state.castlingrights = parsed[2]
    state.targetsquare = parsed[3]
    state.halfmoveclock = parsed[4]
    state.fullmove = parsed[5]
    if (len(parsed) > 6):
        state.move = (int(parsed[6]), int(parsed[7]))
    processFenStr(plateStrFen, state.chessPlate)

def processFenStr(line : str, plate):
    plateRows : list[str] = line.split("/")
    for row in plateRows:
        newRow : list[list] = []
        for char in row:
            if char.isnumeric():
                    for i in range(int(char)):
                        newRow.append('.')
            else:
                newRow.append(char)
        plate.append(newRow)
