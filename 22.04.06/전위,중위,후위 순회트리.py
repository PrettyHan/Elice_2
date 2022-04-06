'''
preorder, inorder, postorder 함수를 구현하세요.
'''

def preorder(tree) :
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    # 순회를 한 결과 방문한 노드들을 순서대로 담고있는 리스트 result
    # result 값 추가 = 현재 노드를 방문
    result = []
    
    
    #[루트노드] + [왼쪽 전위순회] + [오른쪽 전위순회]
    result.append(tree.index)
    if tree.left != None :
        result = result + preorder(tree.left)
    if tree.right != None :
        result = result + preorder(tree.right)
    return result

def inorder(tree) :
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    #[왼쪽] + [루트] + [오른쪽]
    if tree.left != None :
        result = result + inorder(tree.left)
    
    result.append(tree.index)
    
    if tree.right != None :
        result = result + inorder(tree.right)
    return result

def postorder(tree) :
    #[왼쪽] + [오른쪽] + [루트]

    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    if tree.left != None :
        result = result + postorder(tree.left)
    
    
    if tree.right != None :
        result = result + postorder(tree.right)
        
    result.append(tree.index)
    
    return result