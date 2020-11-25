#include "compat.h"

int main()
{
	int x;
	x = rand(1, 2);
	while (x > 0) {
		x = x + 1;
	}
        assert(x > 0);
	return 0;
}
// EXPECTED
// assert at line 10: unreachable
