import math
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
                continue
            elif target < nums[mid]:
                right = mid - 1
                continue
        return -1
if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = -1

    sol = Solution()
    ans = sol.search(nums,target)
    print(ans)

        