counter = 0; # global variable keeps the count of the inversions

def findRop(arr):
	global counter;
	mid = len(arr)//2; # mid of size of the  array
	arrA = []; arrB = []; # divided array into 2 halves

	for i in range(mid): 
		arrA.append(arr[i]); # first half of the array
	for i in range(mid,len(arr)):
		arrB.append(arr[i]); # second half of the array

	if (len(arr)>1): 
		findRop(arrA); # recursive call for the 1st part
		findRop(arrB); # recursive call for the 2nd part
		i = 0; j = 0;
		first = arrA; second = arrB;

		for k in range(len(first)+len(second)+1): # for all element of the array
			if (first[i] <= second[j]): # if the element of the right part is larger
				arr[k] = first[i]; # i appended the smaller element into union set
				i += 1; # i increased the index of the left part
				if ((i == len(first)) and (j != len(second))): # for all elementts
					while (j != len(second)): # for all elements of the right part
						k += 1; # union set index is increased 
						arr[k] = second[j]; # larger elements appended in union set
						j += 1; # right part pointer is increased
					break;
			elif (first[i] > second[j]): # if the element of the left part is larger
				arr[k] = second[j]; # i appended the smaller element into union set
				counter += (len(first)-i); # inversion counter increased until second[j] becomes larger
				j += 1; # right part pointer is increased
				if ((j == len(second)) and (i!=len(first))):
					while (i != len(first)): # for all elements of the left part
						k += 1;  # union set index is increased 
						arr[k] = first[i]; # larger elements appended in union set
						i += 1; # left part pointer is increased            
					break;
	return arr;

findRop([2,20,3,41,5,6,7,8,99,1]); ##function called to test
print("The number of reverse order pairs: ", str(counter));