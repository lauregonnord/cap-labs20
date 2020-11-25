#include "libprint.h"

int main(){
  int x;
  x = rand(0, 5);
  if (x != 0)
  {
    if (x != 1)
    {
      x = x - 1;
    }
  }
  else
  {
    x = x + 1;
  }
  assert(x <= 4 && x >= 1);
  return 0;
}
// EXPECTED
// assert at line 17: verified
