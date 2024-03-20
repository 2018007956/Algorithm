class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        for x in s:
            if not x.isalpha() and not x.isnumeric():
                s = s.replace(x, '')
                
        for idx, left in enumerate(s):
            if left != s[len(s)-1-idx]:
                return False
        return True 

sol = Solution()
print(sol.isPalindrome("0P"))