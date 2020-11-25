#include "compat.h"

int main(){
  int i;
  i = 0;
  while (i != 10) {
      i = i+1;
  }
  assert(i>0);
  return 0;
}
// EXPECTED
// assert at line 9: verified
