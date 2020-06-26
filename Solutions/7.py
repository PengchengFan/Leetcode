class Solution:
    def reverse(self, x: int) -> int:
        if not (-2147483648 < int(str(x)[::-1].strip('-')) < 2147483647):
	        return 0
        if str(x)[0] == '-':
            return -int(str(x)[1:][::-1])
        return int(str(x)[::-1])