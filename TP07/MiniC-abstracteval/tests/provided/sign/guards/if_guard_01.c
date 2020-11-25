#include "compat.h"

int main(){
  int x;
  int y;
  y = 10;
  x = rand(-2, 2);
  if (x == 0) {
    y = x;
  }
  else {
    y = 0;
  }
  assert(y == 0);
  return 0;
}
// EXPECTED
// assert at line 14: verified
