/* Note:
    Allocate memory yourself!
*/

#include <stdlib.h>
#include <string.h>

char *dna_strand(const char *dna)
{
    printf("%s\n", dna);
    
    char *dna_return = malloc(strlen(dna)+1);
    strcpy(dna_return, dna);
    
    for(int i = 0; i < strlen(dna); i++) {
      if(dna[i] == 'A') dna_return[i] = 'T';
      else if(dna[i] == 'T') dna_return[i] = 'A';
      else if(dna[i] == 'C') dna_return[i] = 'G';
      else dna_return[i] = 'C';
    }
    
    printf("%s\n", dna_return);
    return dna_return;
}