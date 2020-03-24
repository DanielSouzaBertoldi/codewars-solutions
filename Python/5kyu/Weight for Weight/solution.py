# O(N²), not good :/

def order_weight(strng):
    numbers = strng.split();
    sum = 0
    sum_arr = []
    
    for number in numbers:
        for num in number:
            sum += int(num)
        sum_arr.append(sum)
        sum = 0

    z = [x for _, x in sorted(zip(sum_arr, numbers))]
    return " ".join(z)