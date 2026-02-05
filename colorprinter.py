## color() 함수 사용법
## 예시 : color([글자 색:str], [배경색:str])
## 만약 색을 변경하지 않을 경우 none 을 넣으면 유지가 됩니다.
## 아래에 있는 색깔만 사용 가능합니다.
## black, red, green, yellow, blue, magenta, cyan, white
## 밝은 색을 원할경우 색 앞에 b를 넣으세요.
## 예시 : bblack, bgreen
import sys

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
                print("글자 색을 잘못 넣었습니다.")
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
                print("배경 색을 잘못 넣었습니다.")
                return
    ##
    if tnum != 0:
        print("\033[%dm"%tnum,end="")
    if bnum != 0:
        print("\033[%dm"%bnum,end="")
    
def uncolor():
    print("\033[0m",end="")
def colorprint(text,tc,bc='none'):
    color(tc,bc)
    print(text+"\033[0m")
    uncolor()

try:
    if sys.argv[1] == "--version":
        print("ColorPrinter 1.1.0")
        exit()
    elif sys.argv[1] == "--colors":
        print(ctable)
        print("밝은 색을 원하시면 앞에 b를 넣으세요.")
        exit()
    elif sys.argv[1] == "--help":
        print("--version : 버전 확인\n--colors : 사용 가능한 색 확인\n--help : 도움말")
        exit()
except:
    pass
if __name__ == "__main__" and len(sys.argv) == 0:
    uncolor()
    print(f'ColorPrinter에 오신 것을 환영합니다.\n출력하실 메세지를 입력해 주세요.')
    text = input()
    # 무지개색 출력
    for r_tc in ctable:
        for r_bc in ctable:
            colorprint(text, r_tc, r_bc)
    for r_tc in bctable:
        for r_bc in ctable:
            colorprint(text, r_tc, r_bc)
    for r_tc in ctable:
        for r_bc in bctable:
            colorprint(text, r_tc, r_bc)
    for r_tc in bctable:
        for r_bc in bctable:
            colorprint(text, r_tc, r_bc)