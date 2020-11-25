#include "compat.h"

int main(){
	int x,y;
	x=3;
	y=0;
	assert(x>0);
	assert(x>y);
	assert(y==0);
	assert(x!=0);
	assert(x>=0);
	assert(y<=0);
	return 0;
}

// EXPECTED
// assert at line 7: verified
// assert at line 8: verified
// assert at line 9: verified
// assert at line 10: verified
// assert at line 11: verified
// assert at line 12: verified
