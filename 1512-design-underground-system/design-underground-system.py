class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, start_time = self.checkin[id]

        key = (start, stationName)

        if key not in self.trips:
            self.trips[key] = [0, 0]

        self.trips[key][0] += t - start_time
        self.trips[key][1] += 1

        del self.checkin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.trips[(startStation, endStation)]

        return total / count