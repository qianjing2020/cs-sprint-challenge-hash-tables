"""ex2.
Give a list of tickets, output linked ticket in an order so the 
depart of the next ticket matchs the destination of the current ticket. Find an O(n) solution.
"""

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# use a dictionary to store ticket, as cache[source]=destination
cache = {}

def reconstruct_trip(tickets, length):
    # store ticket in cache, O(n)
    for t in tickets:
        cache[t.source] = t.destination

    # initiate route
    route = cache[None]
    # while not reach the last destination None, O(1)
    while route[-1] is not None:
        # loop through cache, O(n)
        for source, destination in cache.items():
            if source == route[-1]:
                route.append(destination)

    return route
