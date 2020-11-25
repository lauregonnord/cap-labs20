#include "compat.h"

int main() {
  int x;
  x = rand(0,10);
  assert(x != 5);
  assert(x == 0 || x == 10);
  return 0;
}

// EXPECTED
// assert at line 6: failed to verify
// assert at line 7: failed to verify
