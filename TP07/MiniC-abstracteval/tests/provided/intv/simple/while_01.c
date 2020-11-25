#include "compat.h"

int main(){
	int x, y, z;
	x = 0;
	y = 0;
	z = 0;
	while(x < 10){
		x = x + 1;
		y = y - 1;
		z = rand(z - 1, z + 1);
	}
	assert(x >= 0);
	assert(y <= 0);
	return 0;
}
// EXPECTED
// assert at line 13: verified
// assert at line 14: verified
