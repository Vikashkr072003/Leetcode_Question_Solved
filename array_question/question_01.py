# ------Question_01 Solved-----
# move_Zero :- Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements



# Solved :-------
nums = [0, 1, 0, 3, 12]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        result = [0] * n
        insert_pos = 0

        for num in nums:
            if num != 0:
                result[insert_pos] = num
                insert_pos += 1
        
        for i in range(n):
            nums[i] = result[i]
            
