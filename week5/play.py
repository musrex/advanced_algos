def myAppend(array, size, data):
    # array memory allocated
    # size is the logical size of array
    # data to be appended
    if size < len(array):
        array[size] = data
        size += 1
    else:
        array = array + array
        array[size] = data
        size += 1
    return array, size

