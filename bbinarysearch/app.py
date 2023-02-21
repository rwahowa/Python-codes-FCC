#mid=left+(right-left)/2


def bin_search(sample,target):
    '''
    target - the target of search.
    sample - the search data.
    Search for target in sample.
    '''
    left = 0
    right = len(sample)-1 

    while left <= right:
        mid = left + (right-left)//2
        if sample[mid] == target:
            print(f"{sample[mid]} Found at position {mid}")
            return sample[mid]

        elif sample[mid] > target:
            right = mid - 1
            
        else:
             left = mid + 1
    
    print(f"{target} NOT Found!!")
    return -1

#test it to see if it works
sample = [1,2,4,5,6,8,44,345,355,367,690,800,900,1030,2134,5009]

bin_search(sample,54)

bin_search(sample,690) 

# Try with strings
print("\n\n ---- This is just a separator ----\n")
sample = ["John","Mary","Alpha", "Adin", "Rowan","Zeal","Yurg","Owen","Maggy","aaron"]

# First convert list to lower case and sort
lowercase_sample = sorted([x.lower() for x in sample])

# print (lowercase_sample)
# ['aaron', 'adin', 'alpha', 'john', 'maggy', 'mary', 'owen', 'rowan', 'yurg', 'zeal'] 

## Now try the search. When searching convert to lowercase. Can be stored in a variable for real use case

bin_search(lowercase_sample,"Steve".lower())

bin_search(lowercase_sample,"Zeal".lower()) 
