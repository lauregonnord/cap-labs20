#include "compat.h"

int main() {
  int x,y;
  x = rand(-3,3);
  y = 1 / (x * x);
  return 0;
}
// EXPECTED
// Warning div by 0 line 6
