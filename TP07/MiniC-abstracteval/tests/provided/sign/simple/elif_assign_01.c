#include "compat.h"

int main(){
  int x,y;
  x = 0;
  if (x > 0) {
    y = 1;
  }
  else if (x == 0) {
    y = 0;
  }
  else {
    y = -1;
  }
  assert(y==0);
  return 0;
}
// EXPECTED
// assert at line 15: verified

