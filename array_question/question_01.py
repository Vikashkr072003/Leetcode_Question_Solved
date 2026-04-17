# ------Question_01 Solved-----
# move_Zero :- Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements


# Solved :-------


def moveToZero(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    for i in range(j, len(nums)):
        nums[i] = 0

    return nums


arr = [0, 2, 0, 4]
print(moveToZero(arr))
