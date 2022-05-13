from lex import *
from parse import *
from emit import *
import sys

def test():
    input = "+- # This is a comment!\n */"
    lexer = Lexer(input)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()
def Ccompiler():
    print("Teeny Tiny Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter("Ahmed.c")
    parser = Parser(lexer, emitter)

    parser.program()  # Start the parser.
    emitter.writeFile()  # Write the output to file.
    print("Compiling completed.")


def main():
    print("Teeny Tiny Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer and parser.
    lexer = Lexer(input)
    parser = Parser(lexer)

    parser.program() # Start the parser.
    print("Parsing completed.")


Ccompiler()