"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
"""

#tc of this approach is O(n log n ) and space complexity is O(1) 
def contains_duplicate1(nums):
    nums.sort()
    j=0
    for i in range(1,len(nums)):
        if nums[j] == nums[i]:
            return True
        j+=1
    return False
nums1 = [1,2,3,1]
print(contains_duplicate1(nums1))

#In this approach we are create a empty set then every unique element add in set if already element available in set then return True else no unqiue element in List loop is completed then return False 
# This approach time complexity is O(n) ans space complexity O(n) 
def contains_duplicate2(nums):
    val=set()
    for num in nums:
        if num not in val:
            val.add(num)
        else:
            return True
    return False
nums2 = [1,2,3,4]
print(contains_duplicate2(nums2))

nums3 = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate2(nums3))