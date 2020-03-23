def series_sum(n):
    base = 1
    sum = 0
    
    for i in range(0, n):
        sum = sum + 1.0/base
        base += 3
    
    return "{0:.2f}".format(sum)