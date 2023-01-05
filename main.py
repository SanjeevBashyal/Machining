import sys
import os
from antlr4 import *
from GcodeLexer import GcodeLexer
from GcodeParser import GcodeParser
from GcodeExecution import GcodeExecution
from CNC import CNC

path=os.getcwd()

def readInputFile(filename):
    with open(filename) as fn:
        data = fn.read()
    return data

def main(argv):
    input = InputStream(readInputFile(os.path.join(path,'code.txt')))
    lexer = GcodeLexer(input)
    stream = CommonTokenStream(lexer)
    parser = GcodeParser(stream)
    tree = parser.prog()
    cnc=CNC()
    GcodeExecution(cnc).visitProg(tree)

if __name__ == '__main__':
    main(sys.argv)