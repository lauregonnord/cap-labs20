#include "compat.h"

int main(){
	int x;
	x = 2;
	if(x == 2){
		assert(x == 2);
	}
	else{
		assert(x != 2);
	}
	assert(x >= 0);
	return 0;
}

// EXPECTED
// assert at line 7: verified
// assert at line 10: unreachable
// assert at line 12: verified
