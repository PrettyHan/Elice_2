'''
is_stack_sequence 함수를 작성하세요.
'''

def is_stack_sequence(nums) :
    # 1을 push 무적권
    stack = [1]
    
    current = 0
    
    for i in range(2, len(nums) +1) :
        while len(stack) > 0 and stack[-1] == nums[current]:
            stack.pop()
            current += 1
        if len(stack) == 0 or stack[-1] < nums[current]:
            stack.append(i)
        else :
            return "No"

    return "Yes"