#include "compat.h"

int main(){
  assert (rand(1, -1) == 0);
  return 0;
}
// EXPECTED
// assert at line 4: unreachable
