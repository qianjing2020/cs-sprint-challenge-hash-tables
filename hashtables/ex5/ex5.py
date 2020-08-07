"""ex5
Find from a list of file paths contains the file listed in queries
"""
def finder(files, queries):
    # create a dictionary to store tuples:
    # cache[filename] = [file path1, file path2, ...]
    cache = {}
    for path in files:
        # split the file path into a list of path items by "/"
        path_items = path.split('/')
        # find filename:
        filename = path_items[-1]
        cache.setdefault(filename,[]).append(path)
        
    # init result
    result = []
    
    for key, value in cache.items():
        if key in queries:
            result.append(value[0])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
