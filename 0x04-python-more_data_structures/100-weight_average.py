#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum_scores, sum_weight = 0, 0
        for (score, weight) in my_list:
            sum_scores += score*weight
            sum_weight += weight
        return sum_scores / sum_weight
    return 0
