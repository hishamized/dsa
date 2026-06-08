from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        twice = {}

        print("Input nums:", nums)

        for i in range(0, len(nums)):
            twice[i] = False
            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i != j:
                    twice[i] = True
                    twice[j] = True

            print(f"i={i}, nums[i]={nums[i]}, twice[{i}]={twice[i]}")

        print("twice map:", twice)

        for i in range(0, len(nums)):
            if twice[i] == False:
                print("Returning index:", i)
                return nums[i]


# test locally
nums = [2, 2, 1]
print("Final output:", Solution().singleNumber(nums))