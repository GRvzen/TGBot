nums = [1,1,1,3,3,4,3,2,4,2]

def duplicates(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

print(duplicates(nums))