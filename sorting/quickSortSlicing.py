array = [8,2,4,7,1,3,9,6,5]
def sort_array(a):
    l = len(a)
    if l <= 1:
        return a
    i = -1
    j = 0
    pivot = a[l - 1]
    pivotIndex = l - 1
    while j < pivotIndex:
        if a[j] > pivot:
            j = j + 1
        else:
            i = i + 1
            a[j], a[i] = a[i], a[j]
            j = j + 1
    else:
        a[i + 1], a[pivotIndex] = a[pivotIndex], a[i + 1]
        pivotIndex = i + 1
    return sort_array(a[0:pivotIndex]) + [pivot] + sort_array(a[pivotIndex+1: l - 1 + 1])
print(f"Original Array: {array}")
print(f"After sorting: {sort_array(array)}")