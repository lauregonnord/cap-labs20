#include "compat.h"

int main(){
  int x,y;
  x = rand(1, 20);
  y = rand(-2, 7);
  assert(x*y >= -40);
  return 0;
}

// EXPECTED
// assert at line 7: verified
