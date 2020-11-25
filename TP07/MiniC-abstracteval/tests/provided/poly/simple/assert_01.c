#include "compat.h"

int main(){
  int i;
  i = -10;
  assert(i<=0);
  return 0;
}
// EXPECTED
// assert at line 6: verified
