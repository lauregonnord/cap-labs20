#include "compat.h"

int main(){
  int x, y, z;
  int a;
  int b;
  x = 1;
  y = 2+x;
  z = -1 + ((x) - y);
  a = x;
  assert(a > 0);
  return 0;
}

// EXPECTED
// assert at line 11: verified
