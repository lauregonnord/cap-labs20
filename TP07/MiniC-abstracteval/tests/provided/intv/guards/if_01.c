#include "compat.h"

int main(){
  int x, y;
  x = 12;
  y = 0;
  if (x > 0) {x = -1;}
  else if (x > 0) {x = 1; y = 1;}
  else {x = 2;}
  assert(x==-1);
  assert(y==0);
  return 0;
}
// EXPECTED
// assert at line 10: verified
// assert at line 11: verified
