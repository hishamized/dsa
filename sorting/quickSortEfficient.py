array = [8,2,4,7,1,3,9,6,5]
def sort_array(a, start, end):
    if start >= end:
        return a
    i = start - 1
    j = start
    pivot = a[end]
    pivotIndex = end
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
    sort_array(a, start, pivotIndex - 1)
    sort_array(a, pivotIndex + 1, end)
print(f"Original Array: {array}")
sort_array(array, 0, len(array) - 1)
print(f"After sorting: {array}")