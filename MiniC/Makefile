PACKAGE = MiniC
MAINFILE_INTERPRETER = MiniCInterpreter
MAINFILE_COMPILER = MiniCC
#change with your own name:
MYNAME = JohnDoe
DIR = $(shell basename $(PWD))
# To change the allocation strategy, use e.g.:
#   make ALLOC=all_in_mem run
ALLOC=none
# Example: stop at the first failed test:
#   make PYTEST_OPTS=-x tests
PYTEST_OPTS = 
# Run a simple target for a particular file with e.g.
#   make TESTFILE=foo.c run-interpreter
TESTFILE = TP03/tests/provided/examples/test00.c
# Run the whole test infrastructure for a subset of test files e.g.
#   make TEST_FILES='TP03/**/bad*.c' tests
ifdef TEST_FILES
export TEST_FILES
endif

PYTEST_BASE_OPTS=-vv -rs --failed-first --cov=$(PWD) --cov-report=term --cov-report=html

ASM=$(TESTFILE:%.c=%.s)
OBJ=$(TESTFILE:%.c=%.riscv)
TRACE=$(TESTFILE:%.c=%.trace)
SIMU = spike pk
ASSEMBLER=riscv64-unknown-elf-gcc

ifndef ANTLR4
abort:
	$(error variable ANTLR4 is not set)
endif

all: antlr

.PHONY: antlr
antlr MiniCLexer.py MiniCParser.py: $(PACKAGE).g4
	$(ANTLR4) $< -Dlanguage=Python3 -visitor -no-listener

main-deps: MiniCLexer.py MiniCParser.py TP03/MiniCInterpretVisitor.py TP03/MiniCTypingVisitor.py

run-interpreter: $(MAINFILE_INTERPRETER).py main-deps
	python3  $< $(TESTFILE)

.PHONY: run-compile $(ASM)
run-compile: $(ASM)
$(ASM): $(TESTFILE) antlr
	python3 $(MAINFILE_COMPILER).py  --reg-alloc=$(ALLOC) $(TESTFILE)

$(OBJ): $(ASM)
	$(ASSEMBLER) TP04/libprint.s $< -o $@

.PHONY: run-trace $(TRACE)
run-trace: $(TRACE)
	cat $<
$(TRACE): $(OBJ)
	-$(SIMU) $(OBJ) >$@

.PHONY: tests tests-interpret tests-codegen tests-regalloc

tests: tests-interpret



tests-interpret: test_interpreter.py main-deps
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) test_interpreter.py


# Test for naive allocator (also runs test_expect to check // EXPECTED directives):
tests-naive: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py -k 'naive or expect'

# Test for all but the smart allocator, i.e. everything that lab4 should pass:
tests-notsmart: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py -k 'not smart'

# Test just the smart allocation (quicker than tests)
tests-smart: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py -k 'smart'

# Complete testsuite (should pass for lab5):
tests-codegen: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py

tar: clean
	dir=$$(basename $$PWD) && cd .. && \
	tar cvfz "$$dir.tgz" --exclude="*.riscv" --exclude=".git" --exclude=".pytest_cache"  \
	--exclude="htmlcov" "$$dir"
	@echo "Created ../$$(basename $$PWD).tgz"

clean:
	find . \( -iname "*~" -or -iname ".cache*" -or -iname "*.diff" -or -iname "log*.txt" -or -iname "__pycache__" -or -iname "*.tokens" -or -iname "*.interp" \) -print0 | xargs -0 rm -rf \;
	rm -rf *~ $(PACKAGE)Parser.py $(PACKAGE)Lexer.py $(PACKAGE)Visitor.py
