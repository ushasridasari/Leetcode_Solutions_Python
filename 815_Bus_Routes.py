from collections import defaultdict, deque
from typing import List

class Solution:
    # Method to find the minimum number of buses required to travel from source to target
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # ToDo: Write Your Code Here.
        
        if source == target:
            return 0
        # If we are already at the target, no bus is needed.

        stop_to_buses = defaultdict(list)
        # This stores which buses visit each stop.

        for bus in range(len(routes)):
            # Visit every bus one by one.

            for stop in routes[bus]:
                # Visit every stop on the current bus route.

                stop_to_buses[stop].append(bus)
                # Add this bus to the list of buses visiting this stop.

        queue = deque()
        # The queue stores buses that we can take next.

        for bus in stop_to_buses[source]:
            # Find all buses available at the starting stop.

            queue.append((bus, 1))
            # Add each starting bus with a count of 1 bus taken.

        visited_buses = set()
        # This remembers buses we have already checked.

        while queue:
            # Continue while there are buses waiting in the queue.

            current_bus, buses_taken = queue.popleft()
            # Remove the first bus and get its bus number and count.

            if current_bus in visited_buses:
                continue
            # If we already checked this bus, skip it.

            visited_buses.add(current_bus)
            # Mark this bus as already checked.

            if target in routes[current_bus]:
                return buses_taken
            # If this bus visits the target, return the number of buses taken.

            for stop in routes[current_bus]:
                # Check every stop visited by the current bus.

                for next_bus in stop_to_buses[stop]:
                    # Find other buses that visit this same stop.

                    if next_bus not in visited_buses:
                        # Only consider buses that we have not checked yet.

                        queue.append((next_bus, buses_taken + 1))
                        # Add the next bus and increase the bus count by 1.

        return -1  # If target is not reachable, return -1

