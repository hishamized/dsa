
def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = mergeSort(a[:mid])
    right = mergeSort(a[mid:])
    return merge(left, right)

def merge(x, y):
    lx = len(x)
    ly = len(y)
    result = []
    i = 0
    j = 0
    while i != lx  or j != ly :
        if i == lx  and y != ly :
            if j < ly:
                result.append(y[j])
            j += 1
            continue
        if j == ly and i != lx:
            if i < lx:
                result.append(x[i])
            i += 1
            continue
        if x[i] < y[j]:
            if i < lx:
                result.append(x[i])
            if i != lx:
                i += 1
        elif y[j] < x[i]:
            if j < ly:
                result.append(y[j])
            if j != ly:
                j += 1
        else:
            result.append(x[i])
            result.append(y[j])
            if i < lx:
                i += 1
            if j < ly:
                j += 1
    return result
array = [9,8,7,6,5,4,3,3,2,1]
print(mergeSort(array))