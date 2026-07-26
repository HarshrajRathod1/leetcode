"""Given an array nums of integers, return how many of them contain an even number of digits.

 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits."""


# This approach is using loop  inside loop its time complexity is O(n^2) spcae complexity O(1)
def find_number1(nums):
    ans=0
    for num in nums:
        count=0
        while(num>0):
            count+=1
            num=num//10
        if(count%2==0):
            ans+=1
    return ans
        
nums1=[12,345,2,6,7896]
print(find_number1(nums1))

#this is a optimized solution of this problem time complexity O(n) space complexity is O(1)
def find_number2(nums):
    res=0
    for val in nums:
        if(len(str(val))%2==0):
            res+=1
    return res

nums2 = [555,901,482,1771]
print(find_number2(nums2))