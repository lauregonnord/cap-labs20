#include "compat.h"

int main(){
  int x;
  x = -1;
  if (true) {x = 0;}
  if (false) {x = 1;}
  assert(x == 0);
  return 0;
}
// EXPECTED
// assert at line 8: verified
