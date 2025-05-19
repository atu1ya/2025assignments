# Name: YOUR NAME
# Student Number: 23XXXXXX

class Clearance:
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3

    @classmethod
    def from_str(cls, s):
        return getattr(cls, s.upper(), cls.NONE)

def security_route(stations, segments, source, target):
    """Finds the fastest route from source station to target station."""
    # --- No imports except base Python, so no heapq ---
    # Use a custom min-heap priority queue to get O(n log n) performance.
    # Each entry: (time, station, clearance)

    def heap_push(heap, item):
        heap.append(item)
        idx = len(heap) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if heap[idx][0] < heap[parent][0]:
                heap[idx], heap[parent] = heap[parent], heap[idx]
                idx = parent
            else:
                break

    def heap_pop(heap):
        if not heap:
            return None
        heap[0], heap[-1] = heap[-1], heap[0]
        item = heap.pop()
        idx = 0
        length = len(heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < length and heap[left][0] < heap[smallest][0]:
                smallest = left
            if right < length and heap[right][0] < heap[smallest][0]:
                smallest = right
            if smallest != idx:
                heap[idx], heap[smallest] = heap[smallest], heap[idx]
                idx = smallest
            else:
                break
        return item

    # Prepare stations as Clearance values
    max_station = max([source, target] + [max(u, v) for u, v, _, _ in segments]) if segments else max(source, target)
    num_stations = max(len(stations), max_station + 1)
    processed_stations = []
    for s in stations:
        if isinstance(s, int):
            processed_stations.append(s)
        elif isinstance(s, str):
            try:
                processed_stations.append(Clearance.from_str(s))
            except Exception:
                processed_stations.append(Clearance.NONE)
        else:
            processed_stations.append(Clearance.NONE)
    while len(processed_stations) < num_stations:
        processed_stations.append(Clearance.NONE)

    # Build adjacency list
    graph = [[] for _ in range(num_stations)]
    for u, v, t, c in segments:
        if isinstance(c, int):
            cc = c
        elif isinstance(c, str):
            try:
                cc = Clearance.from_str(c)
            except Exception:
                cc = Clearance.NONE
        else:
            cc = Clearance.NONE
        graph[u].append((v, t, cc))

    # Dijkstra's algorithm with manual min-heap priority queue
    dist = {}
    pq = []
    heap_push(pq, (0, source, Clearance.NONE))
    dist[(source, Clearance.NONE)] = 0

    while pq:
        time, station, clearance = heap_pop(pq)
        state = (station, clearance)

        if time > dist.get(state, float('inf')):
            continue

        # Try changing clearance
        offered = processed_stations[station]
        if offered != Clearance.NONE and offered != clearance:
            new_state = (station, offered)
            if time < dist.get(new_state, float('inf')):
                dist[new_state] = time
                heap_push(pq, (time, station, offered))

        # Try moving
        for neighbor, travel_time, required_clearance in graph[station]:
            if clearance >= required_clearance:
                new_time = time + travel_time
                new_state = (neighbor, clearance)
                if new_time < dist.get(new_state, float('inf')):
                    dist[new_state] = new_time
                    heap_push(pq, (new_time, neighbor, clearance))

    # Return best time to target
    min_time = None
    for (s, _), t in dist.items():
        if s == target and (min_time is None or t < min_time):
            min_time = t
    return min_time
