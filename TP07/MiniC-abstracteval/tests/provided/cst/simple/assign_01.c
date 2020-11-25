#include "compat.h"

int main(){
  int a;
  a = 0;
  assert (a == 0);
  a = a + 1;
  assert (a == 1);
  a = -1;
  assert (a == -1);
  a = a + 1;
  assert (a == 0);
  return 0;
}

// EXPECTED
// assert at line 6: verified
// assert at line 8: verified
// assert at line 10: verified
// assert at line 12: verified
