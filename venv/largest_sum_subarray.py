def subarray(arr):
    n = len(arr)
    if n == 0:
        return
    dp = [0] * n
    dp[0] = arr[0]
    max_sum = float('-inf')
    start, start_index, end_index = 0, 0, 0
    for i in range(1, n):
        if dp[i - 1] < 0:
            start = i
            dp[i] = arr[i]
        else:
            dp[i] = arr[i] + dp[i - 1]
        if dp[i] > max_sum:
            max_sum = dp[i]
            start_index = start
            end_index = i
    return arr[start_index:end_index+1]


arr = [1,3,-10,2]
print(subarray(arr))
