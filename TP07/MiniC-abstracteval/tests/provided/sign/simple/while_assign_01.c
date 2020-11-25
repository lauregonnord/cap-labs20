#include "libprint.h"

int main() {
  int x,y;
  x = rand(0, 12);
  y = 42;
  while (x > 0) {
    x = x - 2;
    y = y + 4;
  }
  assert(y>0);
  return 0;
}

// EXPECTED
// assert at line 11: verified
