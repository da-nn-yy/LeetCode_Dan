#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-i):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
# @lc code=end

