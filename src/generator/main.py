#!/usr/bin/env python3

import sys

from src.commandParsing.commandParsing import CommandParsing
from src.generator.Generator import Generator
from src.generator.ParseConfig import ParseConfFile

def main():

    parser = CommandParsing()

    arguments = parser.parse(sys.argv)

    pcf = ParseConfFile(arguments[1])
    pcf.parse()
    configFile = pcf.get_config()

    generator = Generator(configFile['nb_inputs'], configFile['nb_layouts'], configFile['neurons_per_layer'])

    filename = arguments[1].split('.')[0]

    nb_files_to_create = int(arguments[2])
    for i in range(nb_files_to_create) :
        current_filename = filename + '_' + str(i + 1) + '.nn'
        generator.save_network(current_filename)

if __name__ == "__main__":
    main()
