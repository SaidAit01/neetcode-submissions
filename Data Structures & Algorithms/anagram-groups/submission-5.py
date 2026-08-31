class Solution:
    def groupAnagrams(self, strs):  # Note: Added 'self' because it's a class method
        anagram_map = {}
        
        # Loop through each string in the list
        for s in strs:
            count = [0] * 26  # Reset count for the CURRENT string
            
            # Loop through each character in the CURRENT string
            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1
            
            # Convert the list to a tuple so it can be a hash map key
            key = tuple(count)
            
            # Add the string to the appropriate group
            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(s)
        
        # Return the list of lists AFTER processing all strings
        return list(anagram_map.values())

# Test
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))