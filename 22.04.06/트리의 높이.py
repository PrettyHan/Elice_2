'''
getHeight 함수를 작성하세요.
'''

def getHeight(myTree) :
    '''
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    # 루트 노드를 포함해서, 왼쪽, 오른쪽 서브트리를 모두 포함.
    # 왼쪽 서브트리의 높이를 구함
    # 오른쪽 서브트리의 높이를 구함.
    # 두 높이를 비교 한 후, 큰 값 + 1(루트노드)
    
    if myTree == None :
        return 0
    else :
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))
    
    
    
    
    
    
    return 0