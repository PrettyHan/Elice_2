# 지시사항을 참고하여 코드를 작성하세요.

def check_log(log_1p, log_2p):
    for i in log_1p:
        if i.startswith('#'):
            a = log_1p.index(i)
        else:
            a = None
    for v in log_2p:
        if v.startswith('#'):
            b = log_2p.index(v)
        else :
            b = None
    if a and b == None:
        return '1p'
    if b and a == None:
        return '2p'
    elif a > b :
        return '2p'
    else :
        return '1p'

# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
print(check_log(["@회복~","!공격!","!공격!","!공격!","!공격!"], ["@회복~#","!공격!","!공격!","@회복~","#회피"]))
