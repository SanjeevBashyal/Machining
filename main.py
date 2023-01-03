import sys
import os
from antlr4 import *
from SqlLexer import SqlLexer
from SqlParser import SqlParser
from SqlExecution import SqlExecution

path=os.getcwd()

def readInputFile(filename):
    with open(filename) as fn:
        data = fn.read()
    return data

def main(argv):
    input = InputStream(readInputFile(os.path.join(path,'code.txt')))
    lexer = SqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SqlParser(stream)
    tree = parser.prog()
    SqlExecution().visitProg(tree)

if __name__ == '__main__':
    main(sys.argv)