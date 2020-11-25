#include "compat.h"

int main(){
	int a,b,c;
	a = rand(0,12);
	b = rand(-5,5);
	c = a%b;
        if (b>0)
        {
        	c = a%b;
        }
        if (b!=0)
        {
        	c = a%b;
        }
        if (b>0 || b<0)
        {
                c = a%b;
        }
        if (!(b>=0 && b<=0))
        {
                assert(b!=0);
        }
        else
        {
		assert(b==0);
	}
	return 0;
}
//EXPECTED
//Warning mod by 0 line 7
//Warning mod by 0 line 14
//Warning mod by 0 line 18
//assert at line 22: failed to verify
//assert at line 26: verified
