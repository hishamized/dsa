arr = [9,1,8,2,7,3,6,4,5]
l = len(arr)
for j in range(0, l-1):
    for i in range(0, l - 1 - j):
        if arr[i] > arr[i + 1]:
            print(arr)
            arr[i], arr[i+1] = arr[i+1], arr[i]
            
