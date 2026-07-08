class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        first = []
        second = []
        i = 0
        j = 0

        while len(first) < uniqueCnt1 or len(second) < uniqueCnt2:
            print(f"\ni = {i}")
            print(f"before -> first={first}, second={second}")

            if i % divisor1 != 0 and i % divisor2 == 0:
                print("branch 1")
                first.append(i)

            elif i % divisor2 != 0 and i % divisor1 == 0:
                print("branch 2")
                second.append(i)

            elif i % divisor1 != 0 and i % divisor2 != 0 and len(first) == 0:
                print("branch 3")
                first.append(i)

            elif i % divisor1 != 0 and i % divisor2 != 0 and len(second) == 0:
                print("branch 4")
                second.append(i)

            elif i % divisor1 != 0 and i % divisor2 != 0:
                print("branch 5")

                diff1 = i - first[-1]
                diff2 = i - second[-1]

                print(f"diff1={diff1}, diff2={diff2}")

                if diff1 > diff2:
                    second.append(i)
                else:
                    first.append(i)

            print(f"after -> first={first}, second={second}")
            i += 1

        return max(max(first), max(second))


# Driver code
s = Solution()

test_cases = [
    (2,4,8,2),
    (2, 7, 1, 3),
    (3, 5, 2, 1),
    (2, 4, 2, 2),
]

for tc in test_cases:
    print("\n" + "=" * 50)
    print("TEST CASE:", tc)

    try:
        ans = s.minimizeSet(*tc)
        print("ANSWER:", ans)
    except Exception as e:
        print("ERROR:", e)