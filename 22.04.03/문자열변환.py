# 지시사항을 참고하여 코드를 작성하세요.
def fix_dict(input_string):
    a = input_string.split(',')
    b = []
    for word in a:
        word.lower()
        word.replace('!', "")
        print(word)
    return b

# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
print(fix_dict("!!EX!perience, el!EphAnt, E-MAIl"))
