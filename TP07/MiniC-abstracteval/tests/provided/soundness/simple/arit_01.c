#include "compat.h"

int main() {
  int a,b,r;
  a = -1;
  assert(a>0);
  a = rand(12,42);
  assert(a<0);
  b = rand(-3,-1);
  r = a-b;
  assert(r<0);
  r = -a+b;
  assert(r>0);
  b = rand(-50,-10);
  r = a+b;
  assert(r==0);
  return 0;
}

// EXPECTED
// assert at line 6: failed to verify
// assert at line 8: failed to verify
// assert at line 11: failed to verify
// assert at line 13: failed to verify
// assert at line 16: failed to verify
