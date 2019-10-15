##########################################################################
#
#    Tufts University, Comp 160 randSelect coding assignment  
#    randSelect.py
#    randomized selection
#
#    includes functions provided and function students need to implement
#
##########################################################################

from random import *

# TODO: implement this function
# ray is a list of ints
# index is an int
def randSelect(ray, index):
	print("Looking for value with rank", index, "in the array:")
	print(ray);
	pivot_index = randPartition(ray)
	print("its rank is", pivot_index, end='; ')
	if index == pivot_index:
		print("Thus, we recurse on nothing. We are done.")
		return ray[pivot_index]
	if index < pivot_index:
		ray = ray[0:pivot_index]
		print("Thus, we recurse on left.")
		return randSelect(ray, index)
	if index > pivot_index:
		ray = ray[pivot_index+1:len(ray)]
		print("Thus, we recurse on right.")
		return randSelect(ray, index - pivot_index-1)

def randPartition(ray):
	pivot_index = randint(0, len(ray)-1)
	print("Selected", ray[pivot_index], "as the pivot", end='; ')
	ray[pivot_index], ray[len(ray)-1] = ray[len(ray)-1], ray[pivot_index]
	pivot_index = len(ray)-1
	i=0
	while i < len(ray)-1:
		if i == pivot_index:
			break;
		if ray[i] > ray[pivot_index]:
			ray[pivot_index-1], ray[i] = ray[i], ray[pivot_index-1]
			ray[pivot_index-1], ray[pivot_index] = ray[pivot_index], ray[pivot_index-1]
			pivot_index-= 1;
			i -= 1
		i += 1
	return pivot_index
