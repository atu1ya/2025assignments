# Name: ATULYA CHATURVEDI
# Student Number: 24225113
from datetime import date

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def trains_planes(trains, planes):
    """Find what flights can be replaced with a rail journey.

    Initially, there are no rail connections between cities. As rail connections
    become available, we are interested in knowing what flights can be replaced
    by a rail journey, no matter how indirect the route. All rail connections
    are bidirectional.

    Target Complexity: O(N lg N) in the size of the input (trains + planes).

    Args:
        trains: A list of `(date, lcity, rcity)` tuples specifying that a rail
            connection between `lcity` and `rcity` became available on `date`.
        planes: A list of `(code, date, depart, arrive)` tuples specifying that
            there is a flight scheduled from `depart` to `arrive` on `date` with
            flight number `code`.

    Returns:
        A list of flights that could be replaced by a train journey.
    """
    # Collect all cities
    cities = set()
    for t in trains:
        cities.add(t[1])
        cities.add(t[2])
    for p in planes:
        cities.add(p[2])
        cities.add(p[3])

    # Prepare events: (date, type, ...)
    events = []
    for t in trains:
        events.append((t[0], 0, t[1], t[2]))  # 0 for rail
    for idx, p in enumerate(planes):
        events.append((p[1], 1, idx, p[0], p[2], p[3]))  # 1 for flight

    events.sort()  # sorts by date, then type (rail before flight on same day)

    uf = UnionFind()
    result = []
    for event in events:
        if event[1] == 0:
            # rail event
            _, _, a, b = event
            uf.union(a, b)
        else:
            # flight event
            _, _, idx, code, depart, arrive = event
            if uf.find(depart) == uf.find(arrive):
                result.append((code, event[0], depart, arrive))
    return result