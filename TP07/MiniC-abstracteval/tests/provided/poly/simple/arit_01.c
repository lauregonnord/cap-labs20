#include "compat.h"

int main() {
  int a,b,r;
  a = rand(12,42);
  b = rand(-3,-1);
  r = a-b;
  assert(r>0);
  r = a+b;
  assert(r>0);
  r = -a+b;
  assert(r>0);
  assert(r<0);
  return 0;
}

// EXPECTED
// assert at line 8: verified
// assert at line 10: verified
// assert at line 12: failed to verify
// assert at line 13: verified
