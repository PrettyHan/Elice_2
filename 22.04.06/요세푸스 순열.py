'''
josephus_sequence 함수를 작성하세요.
'''

import queue


def josephus_sequence(n, k) :
    # n명의 사람들을 큐로 => 원탁
    q = queue.Queue()
    
    result= []
    
    for i in range(1, n+1):
        q.put(i)
        
    
    while not q.empty():
        for i in range(k):
            num = q.get()
            
            if i == k-1 :
                result.append(num)
            else:
                q.put(num)
    
    return []