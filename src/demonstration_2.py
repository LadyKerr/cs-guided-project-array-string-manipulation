"""
Leetcode #66:
You are given a non-empty array that represents the
digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most 
significant place value is at the beginning of the array. 
Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array 
(except for the number 0 itself).

Example 1:
Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:
Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:
Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.

Todo:
- convert ints in list to str
- then join() str
- then convert str to single int and add 1 to the num
- convert single int to new_list of str
- then convert each str in new_list int
- return the new_list
"""

# method 1 - what's the full time complexity of this?
# str.join() executes in O(n) time, what about everything else?
def plus_one(digits): 
    new_num = int(''.join([str(num) for num in digits])) + 1
    return [ int(num) for num in str(new_num) ]


print(plus_one([1,3,2])) # Output: [1, 3, 3]
print(plus_one([1,3,3])) # Output: [1, 3, 4]
print(plus_one([9,9,9])) # Output: [1, 0, 0, 0]
