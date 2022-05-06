## color() 함수 사용법
## 예시 : color([글자 색:str], [배경색:str])
## 만약 색을 변경하지 않을 경우 none 을 넣으면 유지가 됩니다.
## 아래에 있는 색깔만 사용 가능합니다.
## black, red, green, yellow, blue, magenta, cyan, white
## 밝은 색을 원할경우 색 앞에 b를 넣으세요.
## 예시 : bblack, bgreen

ctable = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
bctable = ["bblack", "bred", "bgreen", "byellow", "bblue", "bmagenta", "bcyan", "bwhite"]
def color(tc,bc):
    try:
        tnum = ctable.index(tc) + 30
    except:
        try:
            tnum = bctable.index(tc) + 90
        except:
            if tc == 'none':
                tnum = 0
            else:
                print("색을 잘못 넣었습니다.")
                return
    try:
        bnum = ctable.index(bc) + 40
    except:
        try:
            bnum = bctable.index(bc) + 100
        except:
            if bc == "none":
                bnum = 0
            else:    
                print("색을 잘못 넣었습니다.")
                return
    ##
    if tnum != 0:
        print("\033[%dm"%tnum)
    if bnum != 0:
        print("\033[%dm"%bnum)
    
def uncolor():
    print("\033[0m")
