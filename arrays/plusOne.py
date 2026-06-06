from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = l - 1
        carry = 0
        pre = []
        if digits[i] < 9:
            digits[i] += 1
            return digits
        while i >= 0:
            if digits[i] < 9:
                break
            if i == 0 and digits[i] == 9:
                digits[i] = 0
                digits.insert(0, 1)
            if i == 0 and digits[i] == 10:
                digits[i] = 0
                digits.insert(0, 1)
            if digits[i] == 10 and i != 0:
                digits[i] = 9
            if digits[i] >= 9 and i not in pre:
                carry = 1
                digits[i] = 0
                digits[i - 1] += carry
                if digits[i - 1] == 9:
                    pre.append(i-1)
                carry = 0
            if i - 1 == 0 and digits[i - 1] <= 9:
                break
            i -= 1

        return digits


# ---- DEBUG DRIVER CODE ----
if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([9,8,9]))
    # test_cases = [
    #     [1, 2, 3],
    #     [9],
    #     [9, 9],
    #     [1, 9, 9],
    #     [8, 9, 9, 9],
    # ]

    # for t in test_cases:
    #     print("Input:", t)
    #     print("Output:", s.plusOne(t.copy()))
    #     print("-" * 30)