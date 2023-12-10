def cheese(cheeseArr, boxCap):
	cost = [];		# variables initialized
	maxPrice = 0;
	for i in range(len(cheeseArr)): cost.append(0);
	# finding costs of the cheese portions
	for i in range(i): cost[i] = cheeseArr[i][1]//cheeseArr[i][0];

	cost.sort(reverse=True); # array sorted reverse order

	for i in range(len(cost)):
		boxWe = cheeseArr[i][0]; # current box weight
		boxPr = cheeseArr[i][1]; # current box price
		if ((boxCap - boxWe) >= 0): # box capacty is not full yet
			maxPrice += boxPr; # curent price appended into result
			boxCap -= boxWe; # remaining capacity of the box
		else:
			portion = boxCap/boxWe; # cut the cheese into pieces
			maxPrice += boxPr*portion; # max price increases at the same rate
			boxCap = int(boxCap-(boxWe*portion)); # box capacity decreases at the same rate
			break;
	return int(maxPrice); # max price returned

# cheese[weight,price]
cheeseArr = [[10,60],[40,40],[20,100],[30,120]];
boxWcap = 50;
print("Maximum price : ", cheese(cheeseArr, boxWcap));
