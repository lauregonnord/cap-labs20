#include "compat.h"

int main() {
	int a,b,c;
	a = rand(1,2);
	b = rand(2,3);
	c = rand(3,4);
	assert(a != a);
	assert(a != b);
	assert(a != c);
  return 0;
}

// EXPECTED
// assert at line 8: failed to verify
// assert at line 9: failed to verify
// assert at line 10: verified
