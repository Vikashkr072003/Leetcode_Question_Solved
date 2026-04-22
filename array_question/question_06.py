# 238. Product of Array Except Self
# Problem :- Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# In this code we will use Prefix and Suffix

# Code ---------------------------


def productSelf(nums):
    n = len(nums)
    result = [1] * n

    # Prefix Product :- Means Before the product

    prefix = 1

    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Suffix Product : Means After the product

    suffix = 1

    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


arr = [1, 2, 3, 4]
print(productSelf(arr))
