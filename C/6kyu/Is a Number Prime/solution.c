#include <stdbool.h>
#include <math.h>

bool is_prime(int num)
{
    if(num <= 1)
      return false;
      
    int max = sqrt(num), ignored[max], freeSpace = 0;
    
    for(int i = 2; i <= max; i++) {
      if(num % i == 0)
        return false;
    }
    
    return true;
}