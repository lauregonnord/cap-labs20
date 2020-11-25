#include "compat.h"

int main() {
  int x;
  x = rand(-1,1);
  while(x != 1)
  {
  	x = 1;
  }
  assert(x > 0);
  return 0;
}
// EXPECTED
// assert at line 10: verified
