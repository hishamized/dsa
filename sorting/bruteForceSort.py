#Brute force sorting
array = [9,1,8,2,7,3,6,4,5]
print(f"Before sorting: {array}")
for i in range(0, len(array)):
    for j in range(i+1, len(array)):
        if array[j] < array[i]:
            array[j], array[i] = array[i], array[j]
print(f"After sorting: {array}")