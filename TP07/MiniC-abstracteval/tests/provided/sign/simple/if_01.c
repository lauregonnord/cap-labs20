#include "compat.h"

int main(){
  int x,y;
  x = rand (1, 12);
  assert(x>0);
  if (x > 0) {
    y = 1;
  }
  assert(y>0);
  return 0;
}
// EXPECTED
// assert at line 6: verified
// assert at line 10: verified
