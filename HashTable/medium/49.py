from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            k = ''.join(sorted(w))
            if k not in d:
                d[k] = []
            d[k].append(w)
        return list(d.values())
