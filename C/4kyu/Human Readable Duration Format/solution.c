#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *formatDuration (int n) {
  const char *times[] = {"year", "day", "hour", "minute", "second"};
  unsigned long int timesValues[] = {365 * 24 * 60 * 60, 24 * 60 *60, 60 * 60, 60, 1};
  int timesResults[5];
  int size = 0;
  char *string = calloc(57, sizeof(char));
  char buffer[40];
  char date[8];
  
  if(n == 0)
    return strcpy(string, "now");

  timesResults[0] = n/timesValues[0];
  timesResults[1] = (n-timesValues[0]*timesResults[0])/timesValues[1];
  timesResults[2] = (n-timesValues[0]*timesResults[0]-timesValues[1]*timesResults[1])/timesValues[2];
  timesResults[3] = (n-timesValues[0]*timesResults[0]-timesValues[1]*timesResults[1]-timesValues[2]*timesResults[2])/timesValues[3];
  timesResults[4] = n-timesValues[0]*timesResults[0]-timesValues[1]*timesResults[1]-timesValues[2]*timesResults[2]-timesValues[3]*timesResults[3];

  // Get the size of "valid" times
  for(int i = 0; i < 5; i++) {
    if(timesResults[i] > 0)
      size++;
  }

  // Creating the string to be returned
  for(int i = 0; i < 5; i++) {
    if(timesResults[i] > 0) {
      --size;
      strcpy(date, times[i]);

      if(timesResults[i] > 1)
        strcat(date, "s");

      sprintf(buffer, "%d %s", timesResults[i], date);
      strcat(string, buffer);

      if(size > 1)
        strcat(string, ", ");
      else if (size == 1)
        strcat(string, " and ");
    }
  }

  return string;
}