#include "compat.h"

int main(){
	int a,b,c;
	a = rand(0,12);
	b = rand(-5,5);
	c = a%b;
        if (b!=0)
        {
        	c = b%a;
        }
	return 0;
}
//EXPECTED
//Warning mod by 0 line 7
//Warning mod by 0 line 10
