# Name: YOUR NAME
# Student Number: 23XXXXXX

from enum import IntEnum


class Clearance(IntEnum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3


def security_route(stations, segments, source, target):
    """Finds the fastest route from source station to target station.

    You start with no security clearance.
    When at a security station, you may choose to set your clearance to the same
    as that of the station.
    Each segment gives how long it takes to get from one station to another, and
    what clearance is required to be able to take that segment.

    Target Complexity: O(N lg N) in the size of the input (stations + segments).

    Args:
        stations: A list of what clearance is available at each station, or
            `NONE` if that station can not grant any clearance.
        segments: A list of `(u, v, t, c)` tuples, each representing a segment
            from `stations[u]` to `stations[v]` taking time `t` and requiring
            clearance `c` (`c` may be `NONE` if no clearance is required).
        source: The index of the station from which we start.
        target: The index of the station we are trying to reach.

    Returns:
        The minimum length of time required to get from `source` to `target`, or
        `None` if no route exists.
    """
    import heapq
    
    # Initialize distances
    distances = {}
    for station in range(len(stations)):
        for clearance in list(Clearance):
            distances[(station, clearance)] = float('inf')
    
    # Start at the source with NONE clearance
    distances[(source, Clearance.NONE)] = 0
    pq = [(0, source, Clearance.NONE)]  # (time, station, clearance)
    
    while pq:
        time, station, clearance = heapq.heappop(pq)
        
        # If we've found a longer path to this (station, clearance), skip
        if time > distances[(station, clearance)]:
            continue
        
        # If we've reached the target, return the time
        if station == target:
            return time
        
        # Option 1: Update clearance at the current station
        station_clearance = stations[station]
        if station_clearance != Clearance.NONE:
            if time < distances[(station, station_clearance)]:
                distances[(station, station_clearance)] = time
                heapq.heappush(pq, (time, station, station_clearance))
        
        # Option 2: Move to a neighboring station
        for u, v, t, c in segments:
            if u == station and clearance >= c:  # We can take this segment
                new_time = time + t
                if new_time < distances[(v, clearance)]:
                    distances[(v, clearance)] = new_time
                    heapq.heappush(pq, (new_time, v, clearance))
    
    # If we can't reach the target, return None
    return None
