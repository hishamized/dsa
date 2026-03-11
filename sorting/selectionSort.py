from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min = float('inf')
        minIndex = -1
        for i in range(0, len(nums)):
            min = nums[i]
            for j in range(i, len(nums)):
                if nums[j] < min:
                    min = nums[j]
                    minIndex = j
            if min < nums[i]:
                temp = nums[i]
                nums[i] = min
                nums[minIndex] = temp
        return nums
            
if __name__ == "__main__":
    nums = [5,3,2,1]
    sol = Solution()
    sorted_nums = sol.sortArray(nums)
    print(sorted_nums)