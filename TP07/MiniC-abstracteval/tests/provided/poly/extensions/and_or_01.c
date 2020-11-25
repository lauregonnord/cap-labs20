#include "compat.h"

int main(){
  int x;
  x = rand(0, 5);
  if (x >= 2 && x <= 4)
  {
    x = x - 2;
  }
  else
  {
    x = x - 3;
    if (x < 0) {x=0;}
  }
  if (x < 0 || x == 0)
  {
    x = 1;
  }
  assert(x <= 3 && x > 0);
  return 0;
}
// EXPECTED
// assert at line 19: verified
