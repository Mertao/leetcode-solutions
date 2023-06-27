class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        symbols = ''
        result = 0
        for x in s:
            if x not in symbols:
                symbols += x
            else:
                symbols = symbols[symbols.index(x)+1:] + x
            if len(symbols) > result:
                result = len(symbols)

        return result
