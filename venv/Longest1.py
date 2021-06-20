def longest1(arr):

	n = len(arr)
	dp=[0] *n
	dp[0] = arr[0]
	global_max = float('-inf')
	if n == 0:
		return
	for i in range (n):
		if arr[i] ==1:
			dp[i] = dp[i-1] + 1
		else:
			dp[i] = 0
		if dp[i] > global_max:
			global_max = dp[i]
	return global_max

arr=[1,0,0,0,1,1,1,1,1,0]
print(longest1(arr))