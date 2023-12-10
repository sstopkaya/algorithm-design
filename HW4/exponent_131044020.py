def BruteExp(num, exp):
	result = 1;
	for i in range(exp):	# I multiply the number by itself exp times 
		result *= num;
	return result;

def divCon(num,exp):
	if exp == 0:
		return 1;
	else:
		rec = divCon(num,exp//2);	# problem is divided 2 halves
		if (exp%2 == 0):			# if exponential num is even
			return rec*rec;		# I multiply 2 halves
		return rec*rec*num;		# if it is odd, I multiply 2 halves and the number

#test
print("Brute-Force Result: ", BruteExp(2,5));
print("Divide&Conquer Result: ", divCon(2,5));