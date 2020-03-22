class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(bin(n)[2:]).zfill(32)[::-1], 2)

s = Solution()
print(s.reverseBits(int("00000010100101000001111010011100", 2)))