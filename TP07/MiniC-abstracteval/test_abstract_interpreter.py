#! /usr/bin/env python3
import pytest
import glob
import os
import sys
from test_expect_pragma import TestExpectPragmas, cat

HERE = os.path.dirname(os.path.realpath(__file__))
if HERE == os.path.realpath('.'):
    HERE = '.'
TEST_DIR = HERE
IMPLEM_DIR = HERE

if 'IMPLEM_DIR' in os.environ:
    IMPLEM_DIR = os.environ['IMPLEM_DIR']

IGNORE_ERROR_MESSAGE = False
if 'IGNORE_ERROR_MESSAGE' in os.environ:
    IGNORE_ERROR_MESSAGE = True

ENABLE_DOMAIN_SIGN = True
ENABLE_DOMAIN_CST  = False
ENABLE_DOMAIN_INTV = False
ENABLE_DOMAIN_POLY = False

ENABLE_TEST_SIMPLE= True
ENABLE_TEST_GUARDS = True
ENABLE_TEST_EXTENSIONS = True
ENABLE_TEST_SOUNDNESS = True

ALL_FILES = glob.glob('notests.c')
if ENABLE_TEST_SIMPLE:
   ALL_FILES = ALL_FILES + glob.glob('tests/*/all/simple/*.c')
   if ENABLE_TEST_SOUNDNESS:
      ALL_FILES = ALL_FILES + glob.glob('tests/*/soundness/simple/*.c')
if ENABLE_TEST_GUARDS:
   ALL_FILES = ALL_FILES + glob.glob('tests/*/all/guards/*.c')
   if ENABLE_TEST_SOUNDNESS:
      ALL_FILES = ALL_FILES + glob.glob('tests/*/soundness/guards/*.c')
if ENABLE_TEST_EXTENSIONS:
   ALL_FILES = ALL_FILES + glob.glob('tests/*/all/extensions/*.c')
   if ENABLE_TEST_SOUNDNESS:
      ALL_FILES = ALL_FILES + glob.glob('tests/*/soundness/extensions/*.c')

SIGN_FILES = glob.glob('notests.c')
if ENABLE_DOMAIN_SIGN:
   SIGN_FILES = ALL_FILES
   if ENABLE_TEST_SIMPLE:
      SIGN_FILES = SIGN_FILES + glob.glob('tests/*/sign/simple/*.c')
   if ENABLE_TEST_GUARDS:
      SIGN_FILES = SIGN_FILES + glob.glob('tests/*/sign/guards/*.c')
   if ENABLE_TEST_EXTENSIONS:
      SIGN_FILES = SIGN_FILES + glob.glob('tests/*/sign/extensions/*.c')

INTV_FILES = glob.glob('notests.c')
if ENABLE_DOMAIN_INTV:
   INTV_FILES = ALL_FILES
   if ENABLE_TEST_SIMPLE:
      INTV_FILES = INTV_FILES + glob.glob('tests/*/intv/simple/*.c')
   if ENABLE_TEST_GUARDS:
      INTV_FILES = INTV_FILES + glob.glob('tests/*/intv/guards/*.c')
   if ENABLE_TEST_EXTENSIONS:
      INTV_FILES = INTV_FILES + glob.glob('tests/*/intv/extensions/*.c')

CST_FILES = glob.glob('notests.c')
if ENABLE_DOMAIN_INTV:
   CST_FILES = ALL_FILES
   if ENABLE_TEST_SIMPLE:
      CST_FILES = CST_FILES + glob.glob('tests/*/cst/simple/*.c')
   if ENABLE_TEST_GUARDS:
      CST_FILES = CST_FILES + glob.glob('tests/*/cst/guards/*.c')
   if ENABLE_TEST_EXTENSIONS:
      CST_FILES = CST_FILES + glob.glob('tests/*/cst/extensions/*.c')

POLY_FILES = glob.glob('notests.c')
if ENABLE_DOMAIN_INTV:
   POLY_FILES = ALL_FILES
   if ENABLE_TEST_SIMPLE:
      POLY_FILES = POLY_FILES + glob.glob('tests/*/poly/simple/*.c')
   if ENABLE_TEST_GUARDS:
      POLY_FILES = POLY_FILES + glob.glob('tests/*/poly/guards/*.c')
   if ENABLE_TEST_EXTENSIONS:
      POLY_FILES = POLY_FILES + glob.glob('tests/*/poly/extensions/*.c')

# ALL_FILES = glob.glob(TEST_DIR + '/tests/*/assert_all/Ex1*.c') 
#ALL_FILES += glob.glob(TEST_DIR + '/tests/*/assert_all/Ex4*.c')
# SIGN_FILES = ALL_FILES+glob.glob(TEST_DIR + '/tests/*/assert_signs/Ex1*.c')
#SIGN_FILES += glob.glob(TEST_DIR + '/tests/*/assert_signs/Ex3*.c')
#SIGN_FILES += glob.glob(TEST_DIR + '/tests/*/assert_signs/Ex4*.c')
# CST_FILES = glob.glob('notests.c')
#CST_FILES += ALL_FILES + glob.glob(TEST_DIR + '/tests/*/assert_cst/Ex3*.c')
#CST_FILES += glob.glob(TEST_DIR + '/tests/*/assert_cst/Ex4*.c')
# INTV_FILES = glob.glob('notests.c')
#INTV_FILES = ALL_FILES + glob.glob(TEST_DIR + '/tests/*/assert_intv/Ex2*.c')
#INTV_FILES += glob.glob(TEST_DIR + '/tests/*/assert_intv/Ex3*.c')
#INTV_FILES += glob.glob(TEST_DIR + '/tests/*/assert_intv/Ex4*.c')
# POLY_FILES = glob.glob('notests.c')
#POLY_FILES = ALL_FILES+glob.glob(TEST_DIR + '/tests/*/assert_poly/*.c')

# Path setting
if 'TEST_FILES' in os.environ:
    ALL_FILES = glob.glob(os.environ['TEST_FILES'], recursive=True)
MINIC_EVAL = os.path.join(IMPLEM_DIR, 'Main.py')

class TestEval(TestExpectPragmas):

    def evaluate(self, domain, file):
        return self.run_command(['python3', MINIC_EVAL, '--domain',domain,file])

    def abstract_interp(self,domain,filename):
        cat(filename)  # For diagnosis
        expect = self.get_expect(filename)
        eval = self.evaluate(domain,filename)
        if expect:
            assert(eval == expect)

    @pytest.mark.parametrize('filename', SIGN_FILES)
    def test_sign(self, filename):
        self.abstract_interp('sign',filename)

    @pytest.mark.parametrize('filename', CST_FILES)
    def test_cst(self, filename):
        self.abstract_interp('constant',filename)

    @pytest.mark.parametrize('filename', INTV_FILES)
    def test_intv(self, filename):
        self.abstract_interp('interval',filename)

    @pytest.mark.parametrize('filename', POLY_FILES)
    def test_poly(self, filename):
        self.abstract_interp('polyhedron',filename)

if __name__ == '__main__':
    pytest.main(sys.argv)
