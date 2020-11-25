#include "compat.h"

int main(){
  int x, y;
  x = rand(-2,2);
  y = 0;
  assert(x*y==0);
  x = -1;
  y = x*-1*-1;
  assert(x*y>0);
  return 0;
}
// EXPECTED
// assert at line 7: verified
// assert at line 10: verified
