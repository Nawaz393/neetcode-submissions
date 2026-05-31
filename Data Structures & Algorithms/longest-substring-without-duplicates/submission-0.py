class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len=0
        hash_set=set()
        l=0
        for r in range(len(s)):
            if s[r] not in hash_set:
                hash_set.add(s[r])
                max_len=max(max_len,r-l+1)
            else:
                while s[r] in hash_set:
                    hash_set.remove(s[l])
                    l+=1
                hash_set.add(s[r])
            
                 

        return max_len
