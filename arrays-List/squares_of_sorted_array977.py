"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]"""

#this approach is using space complexity O(n) and time complexity is O(n log n) 
def sorted_squares1(nums):
    res=[]
    for val in nums:
        res.append(val**2)
    res.sort()
    return res
nums1=[-4,-1,0,3,10]
print(sorted_squares1(nums1))


#this approach is not using any space, space complexity O(1) time complexity is O(n log n)
def sorted_squares2(nums):
    for index in range(len(nums)):
        nums[index]=nums[index]**2
    nums.sort()
    return nums
nums2=[-7,-3,2,3,11]
print(sorted_squares2(nums2))


#this approach is optimized approach time complexity O(n) space complexity O(n) 
def sorted_squares3(nums):
    n=len(nums)
    left,right,pos=0,n-1,n-1
    ans=[0] * n
    while (left<=right):
        if(abs(nums[left])>abs(nums[right])):
            ans[pos]=nums[left] * nums[left]
            left+=1
        else:
            ans[pos]=nums[right] * nums[right]
            right-=1
        pos-=1
    return ans
nums3=[-7,-3,2,3,11]
print(sorted_squares3(nums3))


