#include "compat.h"

int main(){
  int x, y, z;
  x = rand(3, 3);
  assert(x == 3);
  return 0;
}

// EXPECTED
// assert at line 6: verified
