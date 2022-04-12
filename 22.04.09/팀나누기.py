def make_team(players) :
    '''
    players : 학생들의 정보가 들어있는 리스트.
    
    players 값 예시
    [
        [학생1 이름, 학생1 슈팅, 학생1 드리블],
        [학생2 이름, 학생2 슈팅, 학생2 드리블],
        [학생3 이름, 학생3 슈팅, 학생3 드리블],
        ...
    ]
    '''
    elice = []
    chaser = []
    sh = []
    dr = []
    for data in players:
        sh.append((data[0], data[1]))
        dr.append((data[0], data[2]))
        
    sh.sort(key=lambda x:-x[1])
    dr.sort(key=lambda x:-x[1])
    
    for i in range(len(players)):
        a = sh.pop
        elice.append(a)
        b = dr.pop
        chaser.append(b)
        
    print(elice, chaser)
    
    # 반환값은 두 개의 리스트가 들어있는 튜플이어야 합니다.
    # 첫 번째 리스트는 엘리스 팀, 두 번째 리스트는 체셔 팀의 선수 명단입니다.
    return 