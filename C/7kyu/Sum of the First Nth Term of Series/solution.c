#include <stddef.h>
#include <stdlib.h>

char *series_sum(const size_t n) {
  double result = 0;
  int base = 1;
  char *ret = (char *) malloc(sizeof(char) * 50);
  
  for(int i = 0; i < n; i++) {
    result = result + (1.0/base);
    base += 3;
  }
  
  snprintf(ret, 50, "%.2f", result);
  return ret;
}