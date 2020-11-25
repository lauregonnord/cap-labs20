#include "compat.h"

int main(){
  assert(false);

  // not
  assert(!true);

  // and
  assert(true && false);
  assert(false && true);
  assert(false && false);

  // or
  assert(false || false);

  // some composition
  assert(true && !((!false) || false));

  return 0;
}

// EXPECTED
// assert at line 4: failed to verify
// assert at line 7: failed to verify
// assert at line 10: failed to verify
// assert at line 11: failed to verify
// assert at line 12: failed to verify
// assert at line 15: failed to verify
// assert at line 18: failed to verify
