#include "compat.h"

int main(){
  int x, y;
  x = 1;
  y = 2;

  if (x == y){
    assert(0 == 0);
  }
  if (x != y){
    assert(x == 1);
  }
  if (x <= y){
    assert(x == 1);
  }
  if (x < y){
    assert(x == 1);
  }
  if (x >= y){
    assert(0 == 0);
  }
  if (x > y){
    assert(0 == 0);
  }

  return 0;
}

// EXPECTED
// assert at line 9: unreachable
// assert at line 12: verified
// assert at line 15: verified
// assert at line 18: verified
// assert at line 21: unreachable
// assert at line 24: unreachable
