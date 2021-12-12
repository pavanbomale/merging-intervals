#function that accepts list of lists as arguements
#with return type of list of lists
def merge( intervals: list[list[int]]) -> list[list[int]]:
	if intervals==[]:#if empty list is passed
		return []
	result=[]
	intervals.sort()#sort the intervals on basis of first position
	for i in intervals:#for each interval in list
                #if result is empty or  end time of last interval is smaller tha start time of  current interval
		if result == [] or result[-1][1] < i[0]:
			result.append(i) # intervals are not overlapping  so append this current interval to  list of result
		else:
			result[-1][1] = max(result[-1][1], i[1]) # intervals  are overlapping, so set end time to maximum of  current interval's end time and end time of result's last interval
	return result
print(merge([[1,4],[3,6],[8,10]]))#sorted intervals
print(merge([[5,8],[1,5],[3,9]]))#unsorted intervals
