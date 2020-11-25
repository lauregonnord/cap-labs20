#include "compat.h"

int main(){
  int x,y;
  x = rand(-12, 12);
  y = 1;
  if (x > 0) {
    x = x + 1;
    assert(y>0);
    y = 1 / x;
  } else {
    x = x-1;
  }
  // this prog is safe wrt div by 0
  return 0;
}

// EXPECTED
// assert at line 9: verified
