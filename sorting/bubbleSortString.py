from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        length_heights = len(heights)
        for i in range(0, length_heights - 1):
            for j in range(0, length_heights -1 - i):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
        return names
if __name__ == "__main__":
    heights = [180,165,170]
    names = ["Mary","John","Emma"]

    sol = Solution()
    sorted_names = sol.sortPeople(names, heights)
    print(sorted_names)