# Single Number using XOR
#11.10.26

def singleNumber(nums):
    result=0
    for i in nums:
        result = result^i
    return result


singleNumber([2,2,1])
