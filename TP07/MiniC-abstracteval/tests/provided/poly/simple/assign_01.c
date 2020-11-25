#include "compat.h"

int main(){
  int a, b, c;
  a = rand(0, 5);
  b = a + 1;
  c = a - 1;
  assert(a < b);
  assert(c < a);
  assert(a - 1 == 1*c);
  assert(rand(a+1, a+2) > a);
  return 0;
}
// EXPECTED
// assert at line 8: verified
// assert at line 9: verified
// assert at line 10: verified
// assert at line 11: verified
