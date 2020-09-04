#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
    
    def reverseWords1(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left < right and s[left] == " ":
            left += 1
        while left < right and s[right] == " ":
            right -= 1
        
        d, word = collection.deque(), []

        while left <= right:
            if s[left] == " " and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))

        return " ".join(d)
 
        
# @lc code=end

