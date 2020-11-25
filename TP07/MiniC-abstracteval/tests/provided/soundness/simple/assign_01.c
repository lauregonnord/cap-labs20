#include "compat.h"

int main(){
  int a;
  a = 0;
  assert (a == 1);
  assert (a > 0);
  assert (a < 0);
  a = a + 1;
  assert (a == 0);
  assert (a < 0);
  a = -1;
  assert (a == 0);
  assert (a > 0);
  return 0;
}

// EXPECTED
// assert at line 6: failed to verify
// assert at line 7: failed to verify
// assert at line 8: failed to verify
// assert at line 10: failed to verify
// assert at line 11: failed to verify
// assert at line 13: failed to verify
// assert at line 14: failed to verify
