import MergeSort
import NumList

# create a new NumList and print out contents

listSize = 10000

testList = NumList.NumList(listSize)

print "Pre MergeSort"
for x in testList.my_list:
    print "\t" + repr(x)

testList.my_list = MergeSort.merge_sort(testList.my_list)

print "Post MergeSort"
for x in testList.my_list:
    print "\t" + repr(x)

# pass to merge to sort and print out contents