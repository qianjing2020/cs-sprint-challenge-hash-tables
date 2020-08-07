"""
ex 1.
Find all combinations of w1 and w2 from weights list so that w1 + w0 == limit and w1 > w2
Return the indices of w1, w2
"""

def get_indices_of_item_weights(weights, length, limit):
    # build a indexed list cache as:
    # cache[(idx1,idx2)]= (w1, w2)
    cache = {}

    # loop through weight list:
    for idx1, w1 in enumerate(weights):
        # because w1>w2, so w1 >= limit/2
        # breakpoint()
        w2 = limit - w1
        if w2 > 0:
            try:
                # pythonlist.index(value, start, end)
                # add start from idx1_1 to avoid return first index of duplicated value
                if w1 == w2:
                    idx2 = weights.index(w2, idx1 + 1)            
                else: 
                    idx2 = weights.index(w2)        
                if (w1, w2) not in cache:
                    cache[(w1, w2)] = [idx1, idx2]   
                    
                print(idx1, idx2)             
            except:
                pass    
        
    # if cache is empyt
    if cache == {}:
        return None
    else:
        result =list(cache.values())[0]
        result.sort(reverse=True)
        
        return result
   
