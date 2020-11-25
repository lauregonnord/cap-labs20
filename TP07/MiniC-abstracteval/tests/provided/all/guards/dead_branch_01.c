#include "compat.h"

int main(){
	int x, y;
	
	x = 0;
	
	if(x >= 0){
		assert(x == 0);
	}
	else{
		assert(x != 0);
	}
	
	return 0;
}
// EXPECTED
// assert at line 9: verified
// assert at line 12: unreachable
