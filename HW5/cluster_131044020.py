# I commented out the print parts 
# in case you want to see the solution step by step, 
# I didn't delete it.
def cluster (arr):
	maxProArr = [];
	maxProArr.append(arr[0]); # I initialized max profit array
	maxProfit = maxProArr[0]; # I initialized max profit

	for i in range(1,len(arr)): 	# from 1 until the end of the array
		maxProArr.append(max(arr[i],(maxProArr[i-1]+arr[i]))); # I selected max subarray

		#print("arr[" + str(i) + "]:" + str(arr[i])+" maxProArr[" + str(i-1) +"]+arr[" + str(i) + "]:" + str(maxProArr[i-1] + arr[i]));
		#print("maxProArr[" + str(i) + "] -> " + str(maxProArr[i]));
		#print();
		
		if (maxProArr[i] > maxProfit): 		# finding larger one
			maxProfit = maxProArr[i]; 		# max profit updated

	return maxProfit;

arr = [3,-5,2,11,-8,9,-5];
print("Maximum profit : ", cluster(arr)); # function called
