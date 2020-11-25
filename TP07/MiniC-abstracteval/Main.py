#!/usr/bin/python3
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from MiniCTypingVisitor import MiniCTypingVisitor, MiniCTypeError
from MiniCAbstractVisitor import execute_abstract_interpretation
from DictionaryAbstractValue import DictionaryAbstractValue
from SignLatticeElement import SignLatticeElement
from ConstantLatticeElement import ConstantLatticeElement
from IntervalLatticeElement import IntervalLatticeElement
from PolyhedronAbtractValue import PolyhedronAbstractValue

import argparse
import antlr4


enable_typing = False


def main():
    # command line
    parser = argparse.ArgumentParser(description='Analyze .c files using abstract interpretation.')
    parser.add_argument('path', type=str,help='file to analyze')
    parser.add_argument('-d','--debug',action="store_true",help='turn on debug messages')
    parser.add_argument('-v','--verbose',action="store_true",help='log abstract values')
    parser.add_argument('--domain', default='sign',help='abstract domain to use')
    args = parser.parse_args()

    debug = args.debug

    # lex and parse
    input_s = antlr4.FileStream(args.path, encoding='utf8')
    lexer = MiniCLexer(input_s)
    stream = antlr4.CommonTokenStream(lexer)
    parser = MiniCParser(stream)
    tree = parser.prog()

    # typing Visitor 
    if enable_typing:
        visitor1 = MiniCTypingVisitor()
        try:
            visitor1.visit(tree)
        except MiniCTypeError as e:
            print(e.args[0])
            exit(1)

    if args.domain == 'interval' or args.domain == 'intv' or args.domain == 'i':
        absval = DictionaryAbstractValue(IntervalLatticeElement)
    elif args.domain == 'sign' or args.domain == 's':
        absval = DictionaryAbstractValue(SignLatticeElement)
    elif args.domain == 'constant' or args.domain == 'cst' or args.domain == 'c':
        absval = DictionaryAbstractValue(ConstantLatticeElement)
    elif args.domain == 'polyhedron' or args.domain == 'poly' or args.domain == 'p':
        absval = PolyhedronAbstractValue()
    else:
        print ("unknown domain:", args.domain)
        exit(3)

    outputs = execute_abstract_interpretation(tree,absval,debug)
    outputs.display()

if __name__ == '__main__':
    main()
