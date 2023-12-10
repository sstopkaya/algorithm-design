def partition(arr, left, right):
	pivot = left;
	pivotElmnt = arr[pivot]; 

	while (left < right):
		while (arr[left] < pivotElmnt): left += 1; #compare left - pivot
		while (arr[right] > pivotElmnt): right -= 1; #compare right - pivot

		if (arr[left] == arr[right]): left += 1; 
		elif (left < right):
			arr[left], arr[right] = arr[right], arr[left]; #swap
	return right;

def quick_select(inp, left, right, k):
	if (left == right): #if they are equal
		return inp[left];

	pivotIdx = partition(inp, left, right); #partition called
	length = (pivotIdx-left+1); #find the length the part until pivot

	if (length == k):  
		return inp[pivotIdx];
	elif (k < length):  
		return quick_select(inp, left, (pivotIdx-1), k); #function call for left part
	else:
		return quick_select(inp, (pivotIdx+1), right, (k-length)); #function call for right part

print("The success rate of the first meaningful kth experiment: ");
print(quick_select([2,20,3,41,5,6,7,8,99,1], 0, 9, 4));