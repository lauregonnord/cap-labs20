#include "compat.h"

int main()
{
	int x, y, z;
	x = 10;
	y = rand(0, 10);
	while (x > 0) {
		x = x - 1;
		z = x;
		if (x != 0) {
			assert (x >= 1 && x <= 9);
			x = z;
			x = z;
		}
		if (x != y) {
			assert (x >= 0 && x <= 9);
			x = z;
		}
	}
	return 0;
}
// EXPECTED
// assert at line 12: verified
// assert at line 17: verified
