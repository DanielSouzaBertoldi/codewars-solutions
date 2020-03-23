def nb_year(p0, percent, aug, p):
    years = 0
    percent = percent/100
    while p0 < p:
      years += 1
      p0 = p0 + (p0 * percent) + aug
    return years