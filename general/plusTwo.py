class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        l = len(digits)
        i = l - 1
        # if digits[i] < 9:
        #     digits[i] += 1
        #     return digits
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                break
            if i == 0 and digits[i] == 9:
                digits[i] = 0
                digits.insert(0, 1)
                i -= 1
                break
            if i == 0 and digits[i] < 9:
                digits[i] += 1
                i -= 1
                break
            digits[i] = 0
            if digits[i-1] < 9:
                digits[i - 1] += 1
                if i - 1== 0:
                    break

            else:
                i-= 1
                continue
            i -= 1
        return digits


s = Solution()
# print(s.plusOne([8, 9, 9, 9]))
print(s.plusOne([9,8,9]))