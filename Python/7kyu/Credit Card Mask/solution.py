# return masked string
def maskify(cc):
    if len(cc) < 5:
        return cc
    
    return '#' * int(len(cc)-4) + cc[-4:]