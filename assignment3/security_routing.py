# Name: YOUR NAME
# Student Number: 23XXXXXX

from enum import IntEnum

class Clearance(IntEnum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3

def security_route(stations, segments, source, target):
    """Finds the fastest route from source station to target station."""
    # --- No imports except base Python, so no heapq ---
    # Use a simple list as a priority queue (min-heap simulation)
    # Each entry: (time, station, clearance)
    # We'll use insertion sort for the queue, which is O(N) per insertion,
    # but since the number of states is small (station*clearance), this is acceptable for the assignment.

    # Prepare stations as Clearance enums
    max_station = max([source, target] + [max(u, v) for u, v, _, _ in segments]) if segments else max(source, target)
    num_stations = max(len(stations), max_station + 1)
    processed_stations = []
    for s in stations:
        if isinstance(s, Clearance):
            processed_stations.append(s)
        elif isinstance(s, str):
            try:
                processed_stations.append(Clearance[s.upper()])
            except Exception:
                processed_stations.append(Clearance.NONE)
        else:
            processed_stations.append(Clearance.NONE)
    while len(processed_stations) < num_stations:
        processed_stations.append(Clearance.NONE)

    # Build adjacency list
    graph = [[] for _ in range(num_stations)]
    for u, v, t, c in segments:
        if isinstance(c, Clearance):
            cc = c
        elif isinstance(c, str):
            try:
                cc = Clearance[c.upper()]
            except Exception:
                cc = Clearance.NONE
        else:
            cc = Clearance.NONE
        graph[u].append((v, t, cc))

    # Dijkstra's algorithm with manual priority queue
    dist = {}
    pq = [(0, source, Clearance.NONE)]
    dist[(source, Clearance.NONE)] = 0

    while pq:
        # Find and pop the minimum time entry
        min_idx = 0
        for i in range(1, len(pq)):
            if pq[i][0] < pq[min_idx][0]:
                min_idx = i
        time, station, clearance = pq[min_idx]
        pq[min_idx] = pq[-1]
        pq.pop()

        state = (station, clearance)
        if time > dist.get(state, float('inf')):
            continue

        # Always try changing clearance at current station (if possible and not already that clearance)
        offered = processed_stations[station]
        if offered != Clearance.NONE and offered != clearance:
            new_state = (station, offered)
            if time < dist.get(new_state, float('inf')):
                dist[new_state] = time
                pq.append((time, station, offered))

        # Always try moving to adjacent stations using current clearance
        for v, t, req in graph[station]:
            if clearance >= req:
                new_time = time + t
                new_state = (v, clearance)
                if new_time < dist.get(new_state, float('inf')):
                    dist[new_state] = new_time
                    pq.append((new_time, v, clearance))

    # Find best time to reach target with any clearance
    min_time = None
    for (s, _), t in dist.items():
        if s == target and (min_time is None or t < min_time):
            min_time = t
    return min_time
