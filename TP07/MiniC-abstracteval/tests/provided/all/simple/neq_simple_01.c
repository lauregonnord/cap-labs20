#include "compat.h"

int main() {
  int a,b;
  a = 5;
  b = -9;
  assert(a != b);
  return 0;
}

// EXPECTED
// assert at line 7: verified
