#include "compat.h"

int main(){
	int x;
	x = rand(3,4);
	if (x != 3){
		assert (x==4);
	}
	else{
		assert(x==3);
	}
	return 0;
}

//EXPECTED
//assert at line 7: verified
//assert at line 10: verified
