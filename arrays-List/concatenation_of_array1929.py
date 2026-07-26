"""Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]"""
#optimized solution beacuse its time complexity O(n) ans space complexity is O(1)
def getConcatenation1(nums):
    for i in range(len(nums)):
        nums.append(nums[i])
    return nums
nums1=[1,2,1]
ans1=getConcatenation1(nums1)
print(ans1)


# time compixity O(n) space complexity O(n)
def getConcatenation2(nums):
    return nums+nums
nums2=[1,3,2,1]
ans2=getConcatenation2(nums2)
print(ans2)

#if we want to store result in new array time complexity O(n) space complexity O(n)
def getConcatenation3(nums):
    n=len(nums)
    ans=[0]*(2*n)
    for i in range(n):
        ans[i]=nums[i]
        ans[i+n]=nums[i]
    return ans
nums3=[1,2,3,1]
res=getConcatenation3(nums3)
print(res)
    