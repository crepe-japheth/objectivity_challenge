
def array_swapper(array, index1, index2):
    # this function swap element at the specified indeces
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

    return array

array = [1, 3, 5, 7, 9] # create an array to swap
index1 = 1
index2 = 4

print(f'array to swap is : {array} with indeces {index1} and {index2}')
arr_swap = array_swapper(array, index1, index2)

print(f'swapped array is : {arr_swap}')