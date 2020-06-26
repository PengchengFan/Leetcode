class Solution:
    def countBits(self, num: int) -> List[int]:
        num_bits = [0]
        for i in range(1, num+1):
            num_bits.append(num_bits[i//2] + i % 2)
        return num_bits