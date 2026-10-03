#Two sum using Brute force
#03.10.26

def twosum(nums,target):
    for i in range(len(nums)):
        needed = target - nums[i]
        for j in range(i+1,len(nums)):
            if nums[j]==needed:
                return[i,j]

nums= [2,7,11,15]
target= 9

nums2 = [3,2,4]
target2= 6

nums3 = [3,3]
target3= 6

print(twosum(nums,target))
print(twosum(nums2,target2))
print(twosum(nums3,target3))
