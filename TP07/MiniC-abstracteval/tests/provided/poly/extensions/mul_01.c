#include "compat.h"

int main() {
  int x,y,z,t;
  x = rand(0,10);
  y = 5;
  z = x*y;
  t = y*x;  
  assert(z <= 59);
  assert(t <= 60);
  t = y*y;
  assert(t==25);
  return 0;
}

// EXPECTED
// assert at line 9: verified
// assert at line 10: verified
// assert at line 12: verified
