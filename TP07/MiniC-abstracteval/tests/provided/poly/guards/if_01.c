#include "compat.h"

int main()
{
	int x, y;
	x = rand(0, 1);
	y = rand(1, 2);	
	if(y <= x)
	{
		assert(x == y);
		assert(x == 1);
		assert(y == 1);
	}
	else
	{
		assert(y - x >= 1 && y - x <= 2);
	}

	x = rand(0, 2);
	y = rand(1, 2);
	if(y <= x)
	{
		assert(x == y);
		assert(x == 1);
		assert(y == 1);
	}
	return 0;
}

//EXPECTED
//assert at line 10: verified
//assert at line 11: verified
//assert at line 12: verified
//assert at line 16: verified
//assert at line 23: failed to verify
//assert at line 24: failed to verify
//assert at line 25: failed to verify
