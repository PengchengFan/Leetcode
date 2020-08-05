class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry, cur, ind = 0, 0, 0
        a = a[::-1]
        b = b[::-1]
        while ind < len(a) or ind < len(b):
            cur = carry
            carry = 0
            if ind < len(a):
                cur += int(a[ind])
            if ind < len(b):
                cur += int(b[ind])
            if cur == 2:
                ans += "0"
                carry = 1
            elif cur == 3:
                ans += "1"
                carry = 1
            else:
                ans += str(cur)
            ind += 1
        if carry == 1:
            ans += "1"
        return ans[::-1]

s = Solution()
ans = s.addBinary("1111", "1111")
print(ans)