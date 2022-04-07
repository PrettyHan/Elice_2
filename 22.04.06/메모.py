import heapq

'''
heapSort 함수를 구현하세요.
'''

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
        heapq.top(self.data)


def heapSort(items) :
    '''
    items에 있는 원소를 heap sort하여 리스트로 반환하는 함수를 작성하세요.

    단, 이전에 작성하였던 priorityQueue를 이용하세요.
    '''

    result = []
    
    pq = PriorityQueue()
    
    for item in items :
        pq.push(item)
    
    for i in range(len(items)):
        result.append(pq.top())
        pq.pop()
        
    return result