# Function to perform quicksort for Partition_Version_1 algorithm:(Select the first item of the partition as the pivot)
from lab4.partition import Partition_arr
import time

#Quicksort Version 4 ****************************************************
def Iterative_Quick_Sort(array, low_index, high_index) -> tuple:
    #create stack (from scratch!) and define operational variables
    start = time.time()
    size = high_index - low_index + 1
    stack = [0] * size
    stack_top = -1
    stack_top = stack_top + 1
    stack[stack_top] = low_index
    stack_top = stack_top + 1
    stack[stack_top] = high_index
    comparison_count = 0
    swap_count = 0

    #Pop from stack while stack is NOT empty
    while stack_top >= 0:
        #Pop high_index and low_index
        high_index = stack[stack_top]
        stack_top = stack_top - 1
        low_index = stack[stack_top]
        stack_top = stack_top - 1

        #call Partition function (with respect to quicksort version #)
        partition_value, swap_count_child, comparison_count_child = Partition_arr(array, low_index, high_index)
        comparison_count += comparison_count_child
        swap_count += swap_count_child

        #algorithm will push left side onto stack
        if partition_value - 1 > low_index:
           stack_top = stack_top + 1
           stack[stack_top] = low_index
           stack_top = stack_top + 1
           stack[stack_top] = partition_value - 1

        #algorithm will push right side onto stack
        if partition_value + 1 < high_index:
           stack_top = stack_top + 1
           stack[stack_top] = partition_value + 1
           stack_top = stack_top + 1
           stack[stack_top] = high_index

    run_time = time.time() - start
    if len(array) == 50:
        print('Sort Function')
        print('Sorted Array: ', array)
        print('Swap Count: ', swap_count)
        print('Comparison Count: ', comparison_count)
        print('\n')
    else:
        print('Sort Function')
        print('Swap Count: ', swap_count)
        print('Comparison Count: ', comparison_count)
        print("Run Time: ", run_time)
        print('\n')

    return array, swap_count, comparison_count, run_time





