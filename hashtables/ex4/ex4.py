"""ex4.
Find a positive numbers if a positive number has a corresponding  negative number.
Return all such positive numbers in a list.

"""
def has_negatives(a):    
    # create a dictionary with key value as such:
    # cache[negative number] = its positive twin
    cache = {}

    for number in a:
        if number < 0:
            if number not in cache:
                cache[number] = -number
    
    # init result
    result = []
    # iterate over cache
    for value in cache.values():
        # if value is negative, put the key to result
        if value in a: 
            result.append(value)        

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
