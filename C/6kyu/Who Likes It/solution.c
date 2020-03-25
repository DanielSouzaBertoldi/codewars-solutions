#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>

char* likes(size_t n, const char *const names[n]) {

  char *phrase;
  
  if(n == 0)
    asprintf(&phrase, "no one likes this");
  else if(n == 1)
    asprintf(&phrase, "%s likes this", names[0]);
  else if(n == 2)
    asprintf(&phrase, "%s and %s like this", names[0], names[1]);
  else if(n == 3)
    asprintf(&phrase, "%s, %s and %s like this", names[0], names[1], names[2]);
  else
    asprintf(&phrase, "%s, %s and %zu others like this", names[0], names[1], n-2);

  return phrase;
}