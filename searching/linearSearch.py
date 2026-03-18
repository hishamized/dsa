from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_1 = -1
        index_2 = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    index_1 = i
                    index_2 = j
        return [index_1, index_2]
if __name__ == "__main__":
    nums = [2,9,4,1,7]
    target = 9

    sol = Solution()
    ans = sol.twoSum(nums,target)
    print(ans)