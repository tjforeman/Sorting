# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    merged_arr = sorted(arrA + arrB)
    
    return merged_arr

newarr = [1,4,5]
newarr2 = [2,3,6]
print(merge(newarr2,newarr))
print(merge(newarr,newarr2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    print(f'before: {arr}')
    if len(arr) > 1: 
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        arr = merge(left,right)
        print(f'after: {arr}')

    return arr

list1 = [10, 12 , 56 ,1 , 6 , 9 , 19 , 21 , 4 , 6]
list2 = [79, 23 , 15, 2, 542, 3, 19, 25, 140, 37 ]
print('this is merged list 2',merge_sort(list1))
print('this is merged list 2', merge_sort(list2))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
