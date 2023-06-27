def solution(target, nums):
    dp = [0] * (target+1)
    dp[0] = 1
    for coin in nums:
        for i in range(coin, target+1):
            dp[i] += dp[i - coin]
    return dp[target]


nums = [2, 7, 11, 15]
target = int(input('Enter number: '))
ans = solution(target, nums)
print(ans)
