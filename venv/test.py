
def toString(list):
	return ''.join(list)

def permutation(A, index=0):
	if index == len(A):
		print (toString(A))

	for i in range(index,len(A)):

		A[index], A[i] = A[i], A[index]
		permutation(A,index+1)
		A[index], A[i] = A[i], A[index]

string =list ('abc')

permutation(string,0)