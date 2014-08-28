#input: ordered list A, number num
#output: index of num in A, if num does not exist in A, return -1
def binary_search(A, num):
	left = 0;
	right = len(A) - 1;
	while(left!=right):
		mid = (left + right) / 2;
		v_mid = A[mid];
		if (v_mid == num):
			return mid;
		if (v_mid > num):
			right = mid - 1;
		else:
			left = mid + 1;
	
	if (A[left] == num):
		return left;
	else:
		return -1;
		
	
		
	