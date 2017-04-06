def average(array):
    # your code goes here
    set_arr = set(array)
    sum_total_heights = sum(set_arr)
    total_number_distinct_heights = len(set_arr)
    average = sum_total_heights / total_number_distinct_heights
    return average