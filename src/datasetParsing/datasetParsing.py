#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## MyTorch
## File description:
## datasetParsing
##

import string
import sys

def parseFile(filePath: string):
    file = open(filePath, "r")
    lines = file.readlines()
    file.close()
    for dataLine in lines:
        chessPlate = []
        move = (-1, -1)
        parseLineFen(chessPlate, dataLine)
        print("NEW LINE GETTING PARSED BRO: ")
        print(chessPlate)

def parseLineFen(plate, line : string):
    parsed = line.split(" ")
    plateStr = parsed[0]
    plateRows = plateStr.split("/")
    for row in plateRows:
        newRow = []
        for char in row:
            if char.isnumeric():
                    newRow.append('' * int(char))
            else:
                newRow.append(char)
        plate.append(newRow)

parseFile("test.txt")
