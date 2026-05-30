from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char_count=Counter(s)
        t_char_count=Counter(t)

        for char,freq in s_char_count.items():
            if char not in t_char_count or t_char_count[char]!=freq:
                return False
        return True
        
            
