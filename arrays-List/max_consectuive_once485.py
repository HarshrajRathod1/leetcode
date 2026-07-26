"""Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2"""

def findMaxConsecutiveOnes(nums):
    res=0
    cons=0
    for val in nums:
        if val==1:
            cons+=1
        else:
            res=max(res,cons)
            cons=0
    return res
nums1=[1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums1))

nums2=[1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums2))
        



 