from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dummy = nums.copy()
        nums.clear()
        seen = {}
        l = len(dummy)
        unique = l
        for i in range(0, l):
            if dummy[i] in seen.keys():
                if seen[dummy[i]] == True:
                    # nums.pop(i)
                    unique -= 1
            else:
                nums.append(dummy[i])
            seen[dummy[i]] = True
        return unique


if __name__ == "__main__":
    nums = [1, 1, 2]

    solution = Solution()
    result = solution.removeDuplicates(nums)

    print("Return value:", result)
    print("Modified nums:", nums)