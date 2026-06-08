class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        item = s.split()
        item = "".join(item)
        for ch in item:
            if ch.isalpha() == False or ch == " ":
                pass
            else:
                new.append(ch)
        new = "".join(new)
        new = new.lower()
        print(new)
        return new == new[::-1]

# test
sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")