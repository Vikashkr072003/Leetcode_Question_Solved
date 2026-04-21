# Question :- 189. Rotate Array
# Problem :--  Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# ----------------------------------------------------------------Solved :---------------------------------------


def rotate(nums, k):
    n = len(nums)
    k = k % n

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return nums


arr = [1, 2, 3, 4, 5, 6, 7]
print(rotate(arr, 3))
