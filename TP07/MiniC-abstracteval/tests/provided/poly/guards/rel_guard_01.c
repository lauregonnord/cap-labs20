#include "compat.h"
int main()
{
	int x, y;
	x = rand(0, 1);
	y = rand(1, 2);
	
	if(y <= x) // x = 1 and y = 1
	{
		assert(x == y);
	}
	else
	{
		assert(y >= x + 1 && y <= x + 2);
	}

	return 0;
}

//EXPECTED
//assert at line 10: verified
//assert at line 14: verified
