class Solution:
    def numDecodings(self, s: str) -> int:
        def _numDecodings(s):
            if len(s) == 0:
                return 1
            ch1, ch2 = int(s[0]), 7
            
            if len(s) > 1:
                ch2 = int(s[1])
            
            if ch1 <= 2 and ch2 <= 6:
                return _numDecodings(s[1:]) + _numDecodings(s[2:])
            return _numDecodings(s[1:])

        count = _numDecodings(s)
        return count

s = Solution()
print(s.numDecodings("0"))