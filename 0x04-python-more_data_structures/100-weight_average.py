#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0

    for tup_le in my_list:
        num += (tup_le[0] * tup_le[1])
        den += tup_le[1]
    return num / den
