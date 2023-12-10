def maxCourses(start, finish):
	counter = 1; # num of courses counter starts from 1
				 # because I assumed the first course selected
	i = 0;		 # index for finish array
	for j in range(len(finish)):
		# if the start time of the course is later than the previous one
		if (start[j] >= finish[i]):
			counter += 1; # course can be selected
			i = j;	# synces indexes
	return counter; # num of courses

start = [1,3,0,5,8,5];
finish = [2,4,6,7,9,9];
print("max number of courses : ", maxCourses(start, finish));
