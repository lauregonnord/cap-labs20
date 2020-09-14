#! /usr/bin/env python3
"""
Usage:
    python3 arit2.py <filename>
"""
# Main file for MIF08 - Lab03 - 2018

from Arit2Lexer import Arit2Lexer
from Arit2Parser import Arit2Parser, UnknownIdentifier, DivByZero
from antlr4 import FileStream, CommonTokenStream

import argparse


def main(inputname):
    lexer = Arit2Lexer(FileStream(inputname))
    stream = CommonTokenStream(lexer)
    parser = Arit2Parser(stream)
    try:
        parser.prog()
    except UnknownIdentifier as exc:  # Parser's exception
        print('{} is undefined'.format(exc.args[0]))
        exit(1)
    except DivByZero:
        print('Division by zero')
        exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AritEval lab')
    parser.add_argument('filename', type=str,
                        help='Source file.')
    args = parser.parse_args()
    main(args.filename)
