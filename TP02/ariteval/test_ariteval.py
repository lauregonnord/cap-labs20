#! /usr/bin/env python3
import pytest
import glob
import sys
from test_expect_pragma import TestExpectPragmas

ALL_FILES = glob.glob('./testfiles/hello*.txt')

# only test programs of these shapes!
# ALL_FILES = glob.glob('./testfiles/test*.txt')
# + glob.glob('./testfiles/bad*.txt')

EVAL = 'arit2.py'


class TestEVAL(TestExpectPragmas):
    def evaluate(self, file):
        return self.run_command(['python3', EVAL, file])

    @pytest.mark.parametrize('filename', ALL_FILES)
    def test_expect(self, filename):
        expect = self.get_expect(filename)
        eval = self.evaluate(filename)
        if expect:
            assert(expect == eval)


if __name__ == '__main__':
    pytest.main(sys.argv)
