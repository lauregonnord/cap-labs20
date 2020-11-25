#include "compat.h"

int main() {
  int x;
  x = rand(0,1);
  assert(x==0);
  assert(x==1);
  assert(x>0);
  assert(x<1);
  return 0;
}

// EXPECTED
// assert at line 6: failed to verify
// assert at line 7: failed to verify
// assert at line 8: failed to verify
// assert at line 9: failed to verify
