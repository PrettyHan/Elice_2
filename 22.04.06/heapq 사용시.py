import heapq

class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = []

    def push(self, value) :
        heapq.heappush(self.data, value)

    def pop(self) :
        if len(self.data) > 0 :
            heapq.heappop(self.data)

    def top(self) :
        if len(self.data) == 0 :
            return -1
        else :
            return self.data[0]


