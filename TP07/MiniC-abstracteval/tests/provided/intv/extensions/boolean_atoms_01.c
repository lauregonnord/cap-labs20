#include "compat.h"

int main(){
    int x;
    x = 10;
    while ((x > 0) || false) {
	if (true) {
	    x = x-2;
	}
    }
    assert(x <= 0);
    assert(true);
    assert(false);
    return 0;
}
// EXPECTED
// assert at line 11: verified
// assert at line 12: verified
// assert at line 13: failed to verify

