#include "compat.h"

int main() {
  int r;
  r = rand(12,42);
  assert(r>0);
  r = rand(0,0);
  assert(r==0);
  r = rand(-12,-10);
  assert(r<0);
  r = rand(-3,3);
  assert(r>0);
  r = rand(3,-3);
  assert(r>0);
  return 0;
}

// EXPECTED
// assert at line 6: verified
// assert at line 8: verified
// assert at line 10: verified
// assert at line 12: failed to verify
// assert at line 14: unreachable
