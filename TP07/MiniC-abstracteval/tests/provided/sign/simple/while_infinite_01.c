#include "compat.h"

int main(){
  int x;
  x = 12;
  while (x > 0) {
      x = x+1;
  }
  assert(x==0);
  return 0;
}
// EXPECTED
// assert at line 9: unreachable
