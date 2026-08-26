from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for s in strs:
            # Count frequencies of each letter (a-z)
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Convert list to tuple to use it as a dictionary key
            ans[tuple(count)].append(s)
            
        return list(ans.values())