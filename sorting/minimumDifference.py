from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        minDiff = float('inf')
        #print(nums)
        sort_array(nums, 0, len(nums) - 1)
        #print(nums)
        for i in range(0, len(nums) - k + 1):
            for j in range(i, i + k):
                candidate = nums[i + k - 1] - nums[i]
                if candidate < minDiff:
                    minDiff = candidate
        print(minDiff)
        return minDiff
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
if __name__ == "__main__":
    nums = [9,4,1,7]

    sol = Solution()
    min = sol.minimumDifference(nums,3)
    print(min)