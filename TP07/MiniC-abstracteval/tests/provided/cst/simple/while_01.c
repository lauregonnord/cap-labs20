#include "compat.h"

int main(){
  int x,y;
  x = 12;
  y = 30;
  while (x < y) {
    assert(x<y);
  }
  assert(x<y);
  return 0;
}
// EXPECTED
// assert at line 8: verified
// assert at line 10: unreachable
