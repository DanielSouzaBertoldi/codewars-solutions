# I don't know why I chose to solve this with a dictionary.
# Very unnecessary since we could only count the number of times
# a number appears in the sequence and then check the rest of the
# division by 2. If it's not 0, then it is the odd int. Oh well.

def find_it(seq):
    hash = {}
    
    for x in seq:
        if x in hash:
            hash[x] += 1
        else:
            hash[x] = 1
    
    for y in hash:
        if hash[y] % 2 == 1:
            return y

    return 0