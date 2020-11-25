#include "compat.h"

int main(){

  int x;
  x = rand(0,10000000); //use widening!
  assert(x >= 0);
  while (x > 0) {
    x = x-1;
    assert(x>=0);
  }

 return 0;
}
//EXPECTED
//assert at line 7: verified
//assert at line 10: verified
