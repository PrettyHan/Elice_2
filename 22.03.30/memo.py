





def filter_by_text(text) :
    # 지시사항을 참고하여 코드를 작성하세요.
    freq = text.split('/')[1]
    i = text.split('/')[0]
    
    return sorted(text, key = freq)


# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
print(filter_by_text('a'))