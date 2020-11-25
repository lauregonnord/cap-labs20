#include "compat.h"

int main(){
  int x;
  x = 12;
  while (x != 11) {
      x = x;
      x = x-1;
  }
  assert(x==11);
  return 0;
}
// EXPECTED
// assert at line 10: verified
