#include "compat.h"

int main(){
  int x;
  x = rand (0, 0);
  assert(0==0);
  return 0;
}
// EXPECTED
// assert at line 6: verified
