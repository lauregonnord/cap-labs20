#include "compat.h"

int main(){
  int x, y, z;
  x = 0;
  y = 2;
  z = -3;

  assert(x*x == 0);
  assert(x*y == 0);
  assert(x*z == 0);
  assert(y*x == 0);
  assert(y*y == 4);
  assert(y*z == -6);
  assert(z*x == 0);
  assert(z*y == -6);
  assert(z*z == 9);
  return 0;
}


// EXPECTED
// assert at line 9: verified
// assert at line 10: verified
// assert at line 11: verified
// assert at line 12: verified
// assert at line 13: verified
// assert at line 14: verified
// assert at line 15: verified
// assert at line 16: verified
// assert at line 17: verified
