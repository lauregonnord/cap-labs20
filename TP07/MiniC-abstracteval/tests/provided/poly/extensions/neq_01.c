#include "compat.h"

int main(){
	int x,y;
	x = rand(-10000,10000);
	assert(x<=x);
	assert(x!=x+1);
	assert(x!=x*x);
	assert(y!=y+1);
	y = -100000000;
	while (y != x){
		y = y+1;
	}
	assert (x==y);
	return 0;

}
//EXPECTED
//assert at line 6: verified
//assert at line 7: verified
//assert at line 8: failed to verify
//assert at line 9: verified
//assert at line 14: verified

