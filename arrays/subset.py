from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        smaller = []
        greater = []
        counter = 0
        result = []

        print("nums1:", nums1)
        print("nums2:", nums2)

        if l1 > l2:
            counter = l2
            smaller = nums2
            greater = nums1
        elif l2 > l1:
            counter = l1
            smaller = nums1
            greater = nums2
        else:
            counter = l1
            smaller = nums1
            greater = nums2

        print("\nsmaller:", smaller)
        print("greater:", greater)
        print("counter:", counter)

        for i in range(0, counter):
            print("\n--- LOOP ---")
            print("i:", i)

            # IMPORTANT: keeping your original logic (even though it uses counter not i)
            print("checking smaller[counter]:", smaller[counter] if counter < len(smaller) else "OUT OF RANGE")

            if smaller[counter] in greater and smaller[counter] not in result:
                print("ADDING:", smaller[counter])
                result.append(smaller[counter])

        print("\nFINAL RESULT:", result)
        return result


# -------------------- TEST CASE --------------------
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

sol = Solution()
output = sol.intersection(nums1, nums2)

print("\nOUTPUT:", output)