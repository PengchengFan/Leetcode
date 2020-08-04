class Solution:
    def dailyTemperatures(self, T):
        days = [0] * len(T)
        stack = []
        for i, v in enumerate(T):
            while len(stack) > 0 and stack[-1][-1] < v:
                index, _ = stack.pop()
                days[index] = i - index
            stack.append([i, v])
        return days


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
