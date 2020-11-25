#include "compat.h"

int main(){
  assert(true);

  // not
  assert(!false);

  // and
  assert(true && true);

  // or
  assert(true || true);
  assert(true || false);
  assert(false || true);

  // some composition
  assert(true && ((!false) || false));

  return 0;
}

// EXPECTED
// assert at line 4: verified
// assert at line 7: verified
// assert at line 10: verified
// assert at line 13: verified
// assert at line 14: verified
// assert at line 15: verified
// assert at line 18: verified
