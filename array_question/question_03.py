# LeetCode Questions :-- Remove Duplicates from Sorted Array :-
# Code :--

# Approach 1.[Hash Set]


class Solution:
  def removeDuplicates(self, nums: list[list]) -> int:
    unique = sorted(set(nums))

    for i in range(len(unique)):
      nums[i] = unique[i]

    return len(unique)

nums = [1, 1, 2, 2, 3]

obj = Solution()
k = obj.removeDuplicates(nums)

print(k)
print(nums)


# Approach 2 : Using Two Pointers


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        insert_pos = 1

        for i in range(1, len(nums)):
            # Found a new unique value, place it at insert_pos
            if nums[i] != nums[insert_pos - 1]:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        return insert_pos


nums = [1, 1, 2, 2, 3]

obj = Solution()
k = obj.removeDuplicates(nums)

print(k)
print(nums)
