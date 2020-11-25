#include "compat.h"

int main(){
	int x,y,z;
	x=6;
	y=6;
	z=0;
	if((x==5)||(z==0)){
		assert(x==y);
	}
	else if ((x==6)&&(z>0)){
		z = 1; // This should never happen
	}
	assert(z==0);
	return 0;
}

// EXPECTED
// assert at line 9: verified
// assert at line 14: verified
