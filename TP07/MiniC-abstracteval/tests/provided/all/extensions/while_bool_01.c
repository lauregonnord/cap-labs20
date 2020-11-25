#include "compat.h"

int main()
{
	int x;
	while (false) {
		x = 0;
		assert (x==0);
	}
	while (true) {
		x = 0;
		assert (x==0);
	}
	assert (x==0);
	return 0;
}
// EXPECTED
// assert at line 8: unreachable
// assert at line 12: verified
// assert at line 14: unreachable
