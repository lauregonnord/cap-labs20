#include "compat.h"

int main(){
  int x,y;
  x = rand(11, 42);
  y = x + 30;
  assert(y > 40);
  return 0;
}
// EXPECTED
// assert at line 7: verified
