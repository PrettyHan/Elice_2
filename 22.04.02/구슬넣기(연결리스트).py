'''
1. LinkedListPipe 클래스를 완성하세요.
2. procesBeads 함수를 완성하세요.
'''

class LinkedListElement :
    def __init__(self, val, ptr) :
        self.value = val # 정수
        self.myNext = ptr # 또다른 element

class LinkedListPipe:
    '''
    Linked List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        '''
        # 연결 리스트의 시작 정점과 끝 정점을 가리키는 것이
        # 각각 start, end = > none으로 초기화
        self.start = None
        self.end = None
        pass

    def addLeft(self, n) :
        '''
        파이프의 왼쪽으로 구슬 n을 삽입합니다.
        '''
        if self.start == None and self.end ==None :
            elem = LinkedListElement(n, None)
            
            self.start = elem
            self.end = elem
        else:
            elem = LinkedListElement(n, self.start)
            
            self.start = elem

    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        if self.start == None and self.end ==None :
            elem = LinkedListElement(n, None)
            
            self.start = elem
            self.end = elem
        else:
            elem = LinkedListElement(n, None)
            
            self.end.myNext = elem
            
            self.end = elem

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        result = []
        
        current = self.start
        
        while current != None:
            result.append(current.value)
            current = current.myNext
        
        return result

def processBeads(myInput) :
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.

    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우 

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    입니다.

    '''

    myPipe = LinkedListPipe()

    for x, y in myInput :
        if y == 0 :
            myPipe.addLeft(x)
        elif y == 1 :
            myPipe.addRight(x)
    return myPipe.getBeads()

# 지시사항
# 입력
# 입력의 첫 번째 줄에는 구슬의 개수 nnn이 주어집니다. (100≤n≤200000100 \le n \le 200000100≤n≤200000)

# 두 번째 줄부터는 토끼가 구슬을 넣는 행위가 주어집니다.

# 각 줄은 두 개의 정수 aaa, bbb로 이루어지며, 이 뜻은 구슬 aaa를 왼쪽 혹은 오른쪽으로 넣는다는 의미입니다. (1≤a≤10000000001 \le a \le 10000000001≤a≤1000000000)

# (bbb가 0이면 왼쪽, bbb가 1이면 오른쪽이며 그 외의 입력은 주어지지 않는다)

# 출력
# 최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력한다.