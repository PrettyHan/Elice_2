import heapq

class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''
    # 0 * n = 0
    # 0번째 인덱스는 의미가 없음
    
    
    
    def __init__(self) :
        self.data = [0]

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        self.data.append(value)
        
        index = len(self.data) -1
        
        # 마지막으로 삽입한 값이 => 루트노드로 되면 반복 종료
        while index != 1 :
            if self.data[index//2] > self.data[index] :
                temp = self.data[index]
                self.data[index] = self.data[index//2]
                self.data[index//2] = temp
        
                index = index // 2
            else:
                break


    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) == 1:
            return
        # 마지막 노드를 루트 노드 자리로 이동.
        # [1,2,3,4] => [4,2,3,1] => [4,2,3]
        self.data[1] = self.data[-1]
        self.data.pop()
        
        index = 1
        
        while True :
            priority = -1
            # 1. 아무 자식도 없는 경우.
            if len(self.data) -1 < index * 2:
                break
            # 2. 왼쪽 자식만 있는 경우.
            elif len(self.data) - 1 < index * 2 + 1 :
                priority = index * 2
            # 3. 두개의 자식 있는 경우.
            else :
                # 왼쪽 자식이 오른쪽 자식보다 값이 작은 경우
                if self.data[index*2] < self.data[index*2 + 1]:
                    priority = index * 2
                else:
                    priority = index * 2 + 1
            
            if self.data[index] > self.data[priority] :
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp
                
                index = priority
                
            else :
                break

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''

        if len(self.data) == 1 :
            return -1
        else :
            return self.data[1]
        
