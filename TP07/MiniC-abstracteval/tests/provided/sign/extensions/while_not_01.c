#include "libprint.h"

int main(){
  int i;
  i = 10;
  while (! (i < 0)){
    i = i-1;
  }
  assert(i<=0);
  return 0;
}
// EXPECTED
// assert at line 9: verified
