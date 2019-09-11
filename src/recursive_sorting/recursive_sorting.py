'''
def merge( arrA, arrB ):
    print(f"MERGE: {arrA} - {arrB}")
    num_elements = len( arrA ) + len( arrB )
    merged_arr = [0] * num_elements
    # 3. Start merging your single lists of one element together into larger, sorted sets
    # 4. Repeat step 3 until the entire data set has been reassembled
    a_i = 0   # a_i is the current index for arrA
    b_i = 0   # b_i is the current index for arrB
    # for each index in the merged array `elements`...
    for i in range(num_elements):
        # Find the smallest first-item between arrA and arrB
        # Add that to `elements` at the given index
        # Increment the a/b counter
        if a_i >= len(arrA):
            # 1. A is empty, B is not empty
            merged_arr[i] = arrB[b_i]
            b_i += 1
        elif b_i >= len(arrB):
            # 2. B is empty, A is not empty
            merged_arr[i] = arrA[a_i]
            a_i += 1
        elif arrA[a_i] < arrB[b_i]:
            # 3. A has the smaller element
            merged_arr[i] = arrA[a_i]
            a_i += 1
        else: # arrA[a_i] >= arrB[b_i]:
            # 4. B has the smaller element
            merged_arr[i] = arrB[b_i]
            b_i += 1
    print(f"  * MERGED - {merged_arr}")
    return merged_arr
# a_i = 2
# b_i = 0
# i = 2
# arrA[a_i]     arrB[b_i]
# [1, 2, 3]   [4, 5, 6]
# [1, 2, 3, None, None, None]
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # 1. While your data set contains more than one item, split it in half
    # 2. Once you have gotten down to a single element, you have also *sorted* that element
    #    (a single element cannot be "out of order")
    print(f"MERGE SORT: {arr}")
    if len(arr) > 1:
        # Split
        midway_point = len(arr) // 2
        left_arr = arr[: midway_point]
        right_arr = arr[midway_point:]
        # Sort each of the split arrays
        sorted_left = merge_sort(left_arr)
        sorted_right = merge_sort(right_arr)
        # Merge the sorted arrays
        arr = merge(sorted_left, sorted_right)
    return arr
arr = list(range(20))
random.shuffle(arr)
merge_sort(arr)

'''
# TO-DO: complete the help function below to merge 2 sorted arrays


def merge(arrA, arrB):
    print(f"MERGE: {arrA} - {arrB}")
    num_elements = len(arrA) + len(arrB)
    merged_arr = [0] * num_elements
    # Make two variable TRACKERS that will move up each array
    a_i = 0
    b_i = 0
    # Make a for loop that RUNS THE ENTIRE ARRAY (i will be the element we are changing), looks at two values as determined by the trackers and
    # changes the correct element to the smaller value
    for i in range(num_elements):
        # If statement that if arrA[a] is less than arrB[b], merged_arr[i] will be set equal to arrA[a]
        # tracker increments
        if a_i >= len(arrA):
            merged_arr[i] = arrB[b_i]
            b_i += 1
    # elif statement that if arrB[b] is less than arrA[a], merged_arr[i] will be set equal to arrB[b]
    # tracker increments
        elif b_i >= len(arrB):
            merged_arr[i] = arrA[a_i]
            a_i += 1
    # elif statement that if tracker a is greater than or equal to length of array A, then merged_arr[i] will be set equal to arrB[b]
    # tracker for b increments
        elif arrA[a_i] < arrB[b_i]:
            merged_arr[i] = arrA[a_i]
            a_i += 1
    # elif statement that if tracker b is greater than or equal to length of array B, then merged_arr[i] will be set equal to arrA[a]
    # tracker for b increments
        else:
            merged_arr[i] = arrB[b_i]
            b_i += 1
    # now I return merged_arr

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # while your data set contains more than one item, split it in half
    if len(arr) > 1:
        # split
        midway_point = len(arr) // 2
        left_arr = arr[: midway_point]
        right_arr = arr[midway_point:]
        # sort each of the split arrays
        left = merge_sort(left_arr)
        right = merge_sort(right_arr)
        # merge the sorted arrays
        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
