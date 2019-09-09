# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # print(i, "i")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for s in range(i+1, len(arr)):
            # print(s, "s")
            if arr[s] < arr[smallest_index]:
                smallest_index = s

        # TO-DO: swap
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


'''
def selection_sort(arr):                    defines function with array being passed in
    for i in range(0, len(arr) - 1):        setting for loop to go through over each item
        cur_index = i                       setting i as the current index
        smallest_index = cur_index          setting current index as the smallest number

        for s in range(i+1, len(arr)):              setting for loop to look for smallest number
            if arr[s] < arr[smallest_index]:        if this for loop smallest number is smaller than the smallest_index number
                smallest_index = s                  set it as the new smallest_index

        if smallest_index != i:                                             if the smallest_index is not the same as the current top level for loop
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]       swap the places of the numbers 

    return arr
'''

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        # print(i)
        for n in range(0, len(arr) - 1 - i):
            # print(n)
            if arr[n] > arr[n + 1]:
                arr[n], arr[n + 1] = arr[n + 1], arr[n]
    return arr


'''
def bubble_sort(arr):                                       defines function with array being passed in
    for i in range(0, len(arr) - 1):                        setting for loop to go over the array
        for n in range(0, len(arr) - 1 - i ):               setting inner for loop to go over the array minus the current outer loop number
            if arr[n] > arr[n + 1]:                         if the inner loop number is greater than the next number
                arr[n], arr[n + 1] = arr[n + 1], arr[n]     switch the places of the greater and smaller number
    return arr

'''

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
