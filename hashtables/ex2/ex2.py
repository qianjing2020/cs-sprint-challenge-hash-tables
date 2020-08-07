"""ex2.
Give a list of tickets, output linked ticket in an order so the 
depart of the next ticket matchs the destination of the current ticket. Find an O(n) solution.
"""

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    # use a dictionary to store ticket, as cache[source]=destination
    x = {}
    # store ticket in cache, O(n)
    for t in tickets:
        x[t.source] = t.destination

    # initiate route
    route = []
    route.append(x["NONE"])
    # while not reach the last destination None
    while route[-1] != "NONE":
        # find x using last item route as key, and append it
        route.append(x[route[-1]])
    
    return route
