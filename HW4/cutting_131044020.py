##decrease by a constant factor
def cutting(nLenWire):
	mcut=0;
	while True:
		if nLenWire==1: break; #last 1-meter-long piece
		elif nLenWire%2==0: #if num is even
			nLenWire = nLenWire/2;
			mcut = mcut+1; #minimum cut is increased			
		elif nLenWire%2==1: #if num is odd
			nLenWire = (nLenWire+1)/2;
			mcut = mcut+1; #minimum cut is increased
	return mcut;

print("Min cut for 16: ", cutting(16)); #test
print("Min cut for 7: ", cutting(7));
