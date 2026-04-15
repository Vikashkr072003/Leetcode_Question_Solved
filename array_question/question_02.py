# LeetCode Question Number :- 169
# Question :- Majority Element :- Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# example :- 1
# imput : nums = [3,2,3]
# output : 3

# Solved :-


def majority_element(arr):

    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    max_count = 0
    result = None

    for num in freq:
        if freq[num] > max_count:
            max_count = freq[num]
            result = num

    return result


arr = [1, 2, 1, 1, 2]
print(majority_element(arr))
