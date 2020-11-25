#include "compat.h"

int main(){
  int x;
  x = rand(2,95);
  while (x == 10) {
	assert (x==10);
	x = rand(2,95);
  }
  return 0;
}
// EXPECTED
// assert at line 7: verified
