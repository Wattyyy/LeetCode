# https://leetcode.com/problems/design-underground-system

from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        # (start, end) -> [total_time, count]
        self.total_time_dict = defaultdict(list)
        # id -> [(station, checkin_time), (station, checkout_time)]
        self.in_out_dict = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_out_dict[id].append((stationName, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.in_out_dict[id].append((stationName, t))
        start_station, end_station = (
            self.in_out_dict[id][0][0],
            self.in_out_dict[id][1][0],
        )
        start_time, end_time = self.in_out_dict[id][0][1], self.in_out_dict[id][1][1]
        self.total_time_dict[(start_station, end_station)].append(end_time - start_time)
        del self.in_out_dict[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.total_time_dict[(startStation, endStation)]) / len(
            self.total_time_dict[(startStation, endStation)]
        )


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
