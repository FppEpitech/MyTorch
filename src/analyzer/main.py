#!/usr/bin/env python3

import sys

from src.commandParsing.commandParsing import CommandParsing

def main():
    parser = CommandParsing()
    print(parser.parse(sys.argv))
    #TODO: launch analyzer with parsing result

if __name__ == "__main__":
    main()
