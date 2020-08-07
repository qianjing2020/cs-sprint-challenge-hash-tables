"""ex4.
Find a positive numbers if a positive number is followed by a negative number.
Return all such positive numbers in a list.

"""
def has_negatives(a):
    # create a dictionary with key value as such:
    # cache[positive number] = it's next number
    cache = {}
    for idx, number in enumerate(a):
        if number > 0:
            cache[number] = a[idx+1]
    
    # init result
    result = []
    # iterate over cache
    for item in cache:
        # if value is negative, put the key to result
        if item.values() < 0: 
            result.append(item.keys())        

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
