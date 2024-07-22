#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_new = str(x)
        
        re_x_new = x_new[::-1]
        return re_x_new == x_new
# @lc code=end

