#include "compat.h"

int main(){
  int x,y;
  
  //Example of potential unsoundness by overflow
  x = 1000000000 + 1000000000;  
  y = 10 * 1000000000 * 1000000000 + 10 * 1000000000 * 1000000000;  

  assert(x == 2000000000);
  assert(y == 20000000000000000000);

  return 0;
}

// EXPECTED
// assert at line 10: verified
// assert at line 11: verified
