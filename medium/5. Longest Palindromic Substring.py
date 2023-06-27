class Solution:

    def longestPalindrome(self, s: str) -> str:
        result: str = ''
        if self._check_palindrome(s):
            return s
        for i in range(len(s)):
            for j in range(i, len(s)):
                tmp = s[i:j+1]
                check_palindrome: bool = self._check_palindrome(tmp)
                if check_palindrome and len(tmp) > len(result):
                    result = tmp
        return result

    def _check_palindrome(self, s: str) -> bool:
        return s == s[::-1]
