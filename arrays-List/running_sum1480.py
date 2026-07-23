# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

#nums=[1,2,3,4]
#output: [1,3,6,10]

#approach one time compecity is O(n) and also space complxcity is O(n) this is not optimize solution
def running_sum1(nums):
    res=list()
    res.append(nums[0])
    for i in range(1,len(nums)):
        res.append(nums[i]+res[i-1])
    return res

def running_sum2(nums):
    for i in range(1,len(nums)):
        nums[i]+=nums[i-1]
    return nums

nums=[1,2,3,4]
ans1=running_sum1(nums)
ans2=running_sum2(nums)

for val in ans1:
    print(val,end=" ")
print()

for val in ans2:
    print(val,end=" ")

