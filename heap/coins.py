def sol(arr, maxlen):
	dp = [0 for i in range(len(arr)+1)]

	start = arr[0]
	end = arr[-1]



    for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    memo[i] = min(memo[i], 1 + memo[i-c])

    return memo[amount] if memo[amount] != (amount + 1) else -1

arr = [100, -]