#1920. Build Array from Permutation

'''Example 1:

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]'''

# create a new ans array and solve this problem but this problem Time Complexity is O(n) and Space Complexity is O(n)
def build_array1(nums):
    ans=list()
    for i in range(len(nums)):
        """val=nums[i]
        ans.append(nums[val])"""
        ans.append(nums[nums[i]])
    return ans 

nums1=[0,2,1,5,3,4]
res=build_array1(nums1)
print(res)

#we can use list comperations and solve this problem time complexity O(n) space complexity O(n)

def bulid_array2(nums):
    return [nums[nums[i]] for i in range(len(nums))] 

nums2=[5,0,1,2,3,4]
print(bulid_array2(nums2))
