int nbYear(int p0, double percent, int aug, int p) {
  int years = 0;
  percent = percent/100;
  while(p0 < p) {
    years++;
    p0 = p0 + (p0 * percent) + aug;
  }
  return years;
}