class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        fuelLeft = startFuel
        stops = 0
        prevPosition = 0

        for station in stations:
            fuelLeft -= (station[0] - prevPosition)
            while fuelLeft < 0:
                if not heap:
                    return -1
                fuelLeft += -heapq.heappop(heap)
                stops += 1

            heapq.heappush(heap, -station[1])
            prevPosition = station[0]

        fuelLeft -= (target - prevPosition)
        while fuelLeft < 0:
            if not heap:
                return -1
            fuelLeft += -heapq.heappop(heap)
            stops += 1

        return stops