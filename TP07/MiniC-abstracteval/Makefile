PACKAGE = MiniC
MAINFILE = Main
#change with your own name:
MYNAME = JohnDoe
DIR = $(shell basename $(PWD))

TESTFILE?=tests/provided/sign/simple/arit_01.c

ifndef ANTLR4
$(error variable ANTLR4 is not set)
endif

all: main-deps

MiniCLexer.py MiniCParser.py: $(PACKAGE).g4
	$(ANTLR4) $< -Dlanguage=Python3 -visitor -no-listener

main-deps: MiniCLexer.py MiniCParser.py MiniCTypingVisitor.py

run: $(MAINFILE).py main-deps
	python3  $< $(TESTFILE)

# tests all files in ex/test*.c
tests: test_abstract_interpreter.py main-deps
#	TEST_EXTENSIONS=t python3 -m pytest -v --failed-first $< 
	python3 -m pytest -v --failed-first $< 

tar: clean
	dir=$$(basename "$$PWD") && cd .. && \
	tar cvfzh "$$dir.tgz" --exclude="*.riscv" --exclude=".git" --exclude=".pytest_cache"  \
	--exclude="htmlcov" "$$dir"
	@echo "Created ../$$(basename "$$PWD").tgz"

clean:
	rm -rf *~ $(PACKAGE)Parser.py $(PACKAGE)Lexer.py $(PACKAGE)Visitor.py *.pyc *.tokens  __pycache* ex/*~ .cache* ex-types/*~ *.interp tests/assert_all/*.mu tests/assert_cst/*.mu tests/assert_intv/*.mu tests/assert_poly/*.mu tests/assert_signs/*.mu 
