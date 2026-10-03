#Two sum using Hash Map (Dict)
#03.10.26

def twosum(nums,target):
    seen = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return[seen[needed],i]
        seen[nums[i]]=i

nums= [2,7,11,15]
target= 9

nums2 = [3,2,4]
target2= 6

nums3 = [3,3]
target3= 6

print(twosum(nums,target))
print(twosum(nums2,target2))
print(twosum(nums3,target3))
