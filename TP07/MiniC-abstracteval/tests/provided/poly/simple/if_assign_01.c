#include "compat.h"

int main() {
  int u,x;
  u = 4;
  x = 70;
  if (x > 0) {
     u = x;
  }
  assert(u>0);
  return 0;
}

// EXPECTED
// assert at line 10: verified
