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
        if filename not in cache:
            cache[filename] = []
        cache[filename].append(path)
        #cache.setdefault([filename], []).append(path)
    
    # init result
    result = []
    result = [value for value in cache.values() if cache.keys() in queries]
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
