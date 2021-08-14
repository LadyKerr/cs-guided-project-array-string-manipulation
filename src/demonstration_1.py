"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

todo:
- look at inputs & outputs during the understanding phase
- consider the edge cases and the greatest output could be
- the input in an arr of ints
- the output is a int: the index of the item in the arr
- looking at this, this is the arr search problem
- PLAN:
- how to approach looking for something in an arr
- will need to loop thru the arr
- check if currNum is [ivot index
- pivot index:
    - add all nums to the left
    - add all nums to the right
    - compare the nums
    - if they are equal, return index
- return -1
"""

# This is dynamic programming
def pivot_index(nums):
    # method 1 runtime is O(n^2)
    for i in range(len(nums)): #O(n)
        left_sum = sum(nums[ : i]) # sum all nums to the left O(n)
        right_sum = sum(nums[i+1 : ]) #all nums to the right O(n)
        if left_sum == right_sum: #O(1)
            return i #O(1)
    return -1 #O(1)

    #method 2 runtime is O(n)
    left_sum = 0
    right_sum = sum(nums)

    for i in range(len(nums)): #O(n)
        #remove the new value from right_sum first
        right_sum -= nums[i]
        if right_sum == left_sum: #O(1)
             return i #O(1)
        left_sum += nums[i]
    return -1

print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))