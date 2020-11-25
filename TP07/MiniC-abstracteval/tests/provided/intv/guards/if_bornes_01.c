#include "compat.h"


int main() {
	int a,b,c;
	a = rand(1,4);
	b = 4;
	c = 1;
	if (false) {
		assert(true);
	} else {
		assert(true);
	}
	if (a == b) {
		assert(true);
	} else {
		assert(a != 4);
	}
	if (a == c) {
		assert(true);
	} else {
		assert(a != 1);
	}
	return 0;
}
// EXPECTED
// assert at line 10: unreachable
// assert at line 12: verified
// assert at line 15: verified
// assert at line 17: verified
// assert at line 20: verified
// assert at line 22: verified
