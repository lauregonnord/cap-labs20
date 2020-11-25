#include "compat.h"

int main(){
  int x,y;
  x = rand(13,12);
  assert(x <= 13);
  y = rand(13,14);
  assert(13 <= y);
  assert(x <= y);
  return 0;
}
// EXPECTED
// assert at line 6: unreachable
// assert at line 8: unreachable
// assert at line 9: unreachable
