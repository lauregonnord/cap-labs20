#include "compat.h"

int main(){
	int a,b,c;
	a = 5;
	b = a-5;
	c = a%b;
	return 0;
}
//EXPECTED
//Warning mod by 0 line 7
