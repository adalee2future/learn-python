def mergesort(A, head, tail):
	mid = (head + tail) / 2;
	n = tail - head + 1;
	
	if n == 1:
		return [A[head]];
	left = mergesort(A, head, mid);
	right = mergesort(A, mid + 1, tail);
	y = merge(left, right);
	return y;
		

	
def merge(left, right):
	C = [];
	i = 0;
	j = 0;
	left_length = len(left);
	right_length = len(right);
	
	while i < left_length and j < right_length:
		if left[i] < right[j]:
			C = C + [left[i]];
			i = i + 1;
		else:
			C = C + [right[j]];
			j = j + 1;
			
	if i < left_length:
		C = C + left[i:left_length];
	else:
		C = C + right[j:right_length];
	return C;	
