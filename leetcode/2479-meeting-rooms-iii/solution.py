class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()

        rooms = list(range(n))
        heapq.heapify(rooms)

        count_rooms = [0] * n

        running_meetings = []

        for start, end in meetings:

            while running_meetings and running_meetings[0][0] <= start:
                _, room = heapq.heappop(running_meetings)
                heapq.heappush(rooms, room)

            if not rooms:
                end_time, room = heapq.heappop(running_meetings)
                end = end_time + end - start
                heapq.heappush(rooms, room)
            
            room = heapq.heappop(rooms)
            count_rooms[room]+=1
            heapq.heappush(running_meetings, (end, room))

        return count_rooms.index(max(count_rooms))





         


            
        
