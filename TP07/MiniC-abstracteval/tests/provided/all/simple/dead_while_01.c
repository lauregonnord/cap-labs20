#include "libprint.h"

int main(){
  int i,j;
  i = 0; j = 0;
  while (i > 10) {
    if (i <= 0) {
      j = 1;
      i = i+1;
    } else {
      i = i+1;
    }
  }
  assert(j==0);
  assert(j==i);
  return 0;
}
// EXPECTED
// assert at line 14: verified
// assert at line 15: verified
