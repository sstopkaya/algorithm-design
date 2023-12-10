def myWorst(arr, first, last):
    if ((last-first)==1): #for last 2 elements
        if (arr[first]>arr[last]): 
            return arr[first]; #the worst is returned
        else: 
            return arr[last]; #the worst is returned
    # recursively called funciton
    # to find the worst rate in the left part of the list
    # to find the worst rate in the right part of the list
    # to determine which one is worse
    return max(myWorst(arr, first, (first+last)//2), myWorst(arr, (first+last)//2, last));

def myBest(arr, first, last):
    if ((last-first)==1): #for last 2 elements
        if (arr[first]<arr[last]): 
            return arr[first]; #the best is returned
        else: 
            return arr[last]; #the best is returned
    # recursively called funciton
    # to find the best rate in the left part of the list
    # to find the best rate in the right part of the list
    # to determine which one is better
    return min(myBest(arr, first, (first+last)//2), myBest(arr, (first+last)//2, last));

#test
print("worst: ", myWorst([2,20,3,41,5,6,7,8,99,1], 0, 9));
print("best: ", myBest([2,20,3,41,5,6,7,8,99,1], 0, 9));