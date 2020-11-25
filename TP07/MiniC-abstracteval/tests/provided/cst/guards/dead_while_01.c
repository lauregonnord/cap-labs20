#include "compat.h"

int main(){
  int x;
      x = 1;
      while (x == 12) {
	      assert(x == 1);
	  }
  return 0;
 }
// EXPECTED
// assert at line 7: unreachable
