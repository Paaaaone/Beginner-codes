def solve(nums, target):
    if target < min(nums):
        return []
    for i in nums:
        for j in nums:
            if i + j == target:
                return nums.index(i), nums.index(j)


nums = [2, 3]
target = int(input('Enter number: '))
ans = solve(nums,target)
print(ans)
