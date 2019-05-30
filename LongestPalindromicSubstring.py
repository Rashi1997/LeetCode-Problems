class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        N = len(s)
        max_len = 1
        start = 0
        for i in range(N):
            
            if i-max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            
            if i-max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start = i-max_len
                max_len +=1
        
        return s[start:start+max_len]
