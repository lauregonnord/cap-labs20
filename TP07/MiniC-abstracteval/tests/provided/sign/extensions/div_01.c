#include "compat.h"

int main() {
  int a,b,r;
  a = rand(12,42);
  b = rand(-3,-1);
  r = a/b;
  r = (-a)/b;
  r = 0/a;
  r = a/0;
  b = rand(-1,1);
  r = a/b;
  return 0;
}

// EXPECTED
// Warning div by 0 line 10
// Warning div by 0 line 12
