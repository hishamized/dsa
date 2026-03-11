class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        diff = length - min(len(a), len(b))
        if len(a) != len(b):
            if len(a) == length:
                b = '0'*diff + b
            else:
                a = '0'*diff + a
           
        carry = '0'
        result = []
        lastIndex = length - 1
        print(a)
        print(b)
        for i in range(0, length):
            if a[lastIndex - i] == '0' and b[lastIndex - i] == '0' and carry == '0' and i == length-1:
                result.append('0')
                carry = '0'
                print(result)    
            elif a[lastIndex - i] == '1' and b[lastIndex - i] == '0' and carry == '0' and i == length-1:
                result.append('1')
                carry = '0'
                print(result)
            elif a[lastIndex - i] == '0' and b[lastIndex - i] == '1' and carry == '0' and i== length-1:
                result.append('1')
                carry = '0'
                print(result)
            elif a[lastIndex - i] == '1' and b[lastIndex - i] == '1' and carry == '0' and i == length-1:
                result.append('0')
                result.append('1')
                carry = '0'
                print(result)    
            elif a[lastIndex - i] == '0' and b[lastIndex - i] == '0' and carry == '1' and i == length-1:
                result.append('1')
                carry = '0'
                print(result)    
            elif a[lastIndex - i] == '1' and b[lastIndex - i] == '0' and carry == '1' and i == length-1:
                result.append('0')
                result.append('1')
                carry = '0'
                print(result)
            elif a[lastIndex - i] == '0' and b[lastIndex - i] == '1' and carry == '1' and i== length-1:
                result.append('0')
                result.append('1')
                carry = '0'
                print(result)
            elif a[lastIndex - i] == '1' and b[lastIndex - i] == '1' and carry == '1' and i == length-1:
                result.append('1')
                result.append('1')
                carry = '0'
                print(result)
            elif a[lastIndex - i] == '0' and b[lastIndex - i] == '0' and carry == '0':
                result.append('0')
                print(result)
            elif a[lastIndex - i] == '0' and b[lastIndex - i] == '1' and carry == '0':
                result.append('1')
                print(result)
            elif a[lastIndex - i] == '1' and b[lastIndex - i] == '0' and carry == '0':
                result.append('1')
                print(result)
            elif a[lastIndex - i] == '1' and b[lastIndex - i] == '1' and carry == '0':
                carry = '1'
                result.append('0')
                print(result)
            elif a[lastIndex - i] == '0' and b[lastIndex - i] == '0' and carry == '1':
                result.append('1')
                carry = '0'
                print(result)
            elif a[lastIndex - i] == '0' and b[lastIndex - i] == '1' and carry == '1':
                result.append('0')
                carry = '1'
                print(result)
            elif a[lastIndex - i] == '1' and b[lastIndex - i] == '0' and carry == '1':
                result.append('0')
                carry = '1'
                print(result)
            elif a[lastIndex - i] == '1' and b[lastIndex - i] == '1' and carry == '1':
                result.append('1')
                carry = '1'
                print(result)
        result.reverse()
        return "".join(result)
s = Solution()
print(s.addBinary('1010', '11'))