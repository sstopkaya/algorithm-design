def candy(arr, candyLen):
	maxObt = [];
	for i in range(candyLen+1): maxObt.append(0);

	for i in range(1, candyLen+1): # I computed max obt for given candy length
		currMax = -1;
		for j in range(i): # I computed from 0 to the given length
			# all possible pairs that their sum may give the given candy length
			currMax = max(currMax, arr[j]+maxObt[i-j-1]); # select maximum one
		maxObt[i] = currMax; # I fill the DP table with max obt
	return maxObt[candyLen]; # returned max obt of which requested candy length

arr = [1,5,8,9,10,17,17,20];
#test
print("Max obtainable value for 8 cm cand: ", candy(arr, 8));
print("Max obtainable value for 4 cm cand: ", candy(arr, 4));
print("Max obtainable value for 5 cm cand: ", candy(arr, 5));