#include "compat.h"

int main(){
  int x, y, z;
  x = 0;
  y = 1;
  z = -1;

  assert(-x == 0);
  assert(-y == -1);
  assert(-z == 1);

  assert(x+x == 0);
  assert(x+y == 1);
  assert(x+z == -1);
  assert(y+x == 1);
  assert(y+y == 2);
  assert(y+z == 0);
  assert(z+x == -1);
  assert(z+y == 0);
  assert(z+z == -2);

  assert(x-x == 0);
  assert(x-y == -1);
  assert(x-z == 1);
  assert(y-x == 1);
  assert(y-y == 0);
  assert(y-z == 2);
  assert(z-x == -1);
  assert(z-y == -2);
  assert(z-z == 0);

  return 0;
}

// EXPECTED
// assert at line 9: verified
// assert at line 10: verified
// assert at line 11: verified

// assert at line 13: verified
// assert at line 14: verified
// assert at line 15: verified
// assert at line 16: verified
// assert at line 17: verified
// assert at line 18: verified
// assert at line 19: verified
// assert at line 20: verified
// assert at line 21: verified

// assert at line 23: verified
// assert at line 24: verified
// assert at line 25: verified
// assert at line 26: verified
// assert at line 27: verified
// assert at line 28: verified
// assert at line 29: verified
// assert at line 30: verified
// assert at line 31: verified
