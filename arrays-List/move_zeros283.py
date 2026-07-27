"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]"""

#this approach time complexity is high because we are using remove and append
def move_zeros1(nums):
    for val in nums:
        if val==0:
            nums.remove(val)
            nums.append(0)
    return nums
nums1=[0,1,0,3,12]
print(move_zeros1(nums1))

# tc O(n) sc O(n)
def move_zeros2(nums):
    n=len(nums)
    ans=[0] * n
    l=0
    for val in nums:
        if val != 0:
            ans[l]=val
            l+=1
    nums[:]=ans
    return nums
nums2=[0,0,1]
print(move_zeros2(nums2))

#to pointer approach for solving problem time compexity O(n) space complexity is O(1)
def move_zeros3(nums):
    left=0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
    return nums
nums3=[0,1,0,3,12]
print(move_zeros3(nums3))

