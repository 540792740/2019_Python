class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Init two list save save all time of start and end
        start_time, end_time = [], []

        # Save all time into list
        for i, j in intervals:
            start_time.append(i)
            end_time.append(j)

        start_time.sort()
        end_time.sort()

        start_index, end_index = 0, 0
        available_room  , number_room = 0, 0

        while start_index < len(start_time):
            if start_time[start_index] < end_time[end_index]:
                if available_room == 0:
                    number_room += 1
                else:
                    available_room -= 1

                start_index += 1
            else:
                end_index += 1
                available_room += 1

        return number_room

if __name__ == '__main__':
    S = Solution()
    test = S.minMeetingRooms([[0, 30],[5, 10],[15, 20]])
    print(test)