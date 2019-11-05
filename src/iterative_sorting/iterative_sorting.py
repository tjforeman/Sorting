# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        
        # loop though the array
        for j in range(i + 1, len(arr)):

            # if the current index is smaller than the next item in the array assign it
            if arr[smallest_index] > arr[j]:
                smallest_index = j
             


        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # # outer loopy
    # for i in range (len(arr)):
    #     #inner loop over -1 because the last item should be already sorted
    #     for j in range(len(arr) -1):
    #         # compare the value of the iteration to the item to the right
    #         if arr[j] > arr[j+1]:
    #             # if item on left is bigger than item on right then swap
    #             temp = arr[j]
    #             arr[j] = arr[j+1]
    #             arr[j+1] = temp

    did_swap = True

    while did_swap:
        did_swap = False

        for i in range(len(arr) -1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i]= arr[i+1]
                arr[i+1] = temp
                did_swap = True





    return arr

theList = [4,3,2,6,7,1,5,6]

listsorter = bubble_sort(theList)
print(listsorter)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr