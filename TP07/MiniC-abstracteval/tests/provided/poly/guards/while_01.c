#include "compat.h"

int main(){
  int x;
  x = 12;
  while (x > 0) {
      assert (x<=12);
      x = x-1;
  }
  assert(x<=0);
  return 0;
}
// EXPECTED
// assert at line 7: verified
// assert at line 10: verified
