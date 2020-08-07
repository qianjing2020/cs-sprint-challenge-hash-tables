"""ex3.
Find the intersection of all lists, use dict or hash table

"""
# import math

def intersection(arrays):
    # create a dict to store all subarray from input arrays
    puddles = {}
    # puddle index is the array,
    for array in arrays:
        puddles[array] = len(array)

    # init result list with the smallest array
    smallest = min(puddles.values())
    result = [key for key, _ in puddles if puddles.values == smallest]
    # remove the smallest array from puddles
    puddles = {key: value for key,
               value in puddles if puddles.values != smallest}

    # for each number in result, compare it to another puddle, if no match, discard
    for item in result:
        for puddle in puddles:
            if item not in puddle:
                result.remove(item)

    return result



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(100, 200)) + [1, 2, 3])
    arrays.append(list(range(200, 300)) + [1, 2, 3])
    arrays.append(list(range(300, 400)) + [1, 2, 3])

    print(intersection(arrays))
