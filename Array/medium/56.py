from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for interval in sorted(intervals, key=lambda i: i[0]):
            if len(ans) == 0:
                ans.append(interval)
                continue
            lastInterval = ans[-1]
            if lastInterval[1] >= interval[1]:
                continue
            elif lastInterval[1] >= interval[0]:
                lastInterval[1] = interval[1]
            else:
                ans.append(interval)
        return ans

