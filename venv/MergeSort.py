def merge(left, right):
	res = []
	i,j = 0,0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1
	res += left[i:]
	res += right[j:]
	return res


def mergesort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr) //2
	res_left= mergesort(arr[:mid])
	res_right = mergesort(arr[mid:])
	return merge(res_left, res_right)




a = [5,6,7,2,1,0,3]


print(mergesort(a))