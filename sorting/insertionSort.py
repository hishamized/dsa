array = [9,2,8,3,7,4,6,5]
def sort_array(a):
    temp = 0
    l = len(a)
    for i in range(1, l):
        temp = a[i]
        tempIndex = i
        for j in range(i - 1, -1, -1):
            if a[j] > temp:
                #a.insert(j + 1, a.pop(j))
                a[j+1], a[j] = a[j], a[j+1]
            else:
                break
    return a
print(f"Original araay: {array}")
print(f"After sorting: {sort_array(array)}")