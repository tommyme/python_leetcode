class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max = 0
        for start in range(len(s)):
            sub_s = set()
            for end in range(start, len(s)):
                if s[end] not in sub_s:
                    sub_s.add(s[end])
                else:
                    break
            Max = len(sub_s) if len(sub_s) > Max else Max
        return Max
