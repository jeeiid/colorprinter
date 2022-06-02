파이썬에서 print() 에 색을 쉽게 지정하세요!
(주의, 파이썬 기본으로 내장되어있는 idle 에서 작동하지 않습니다, 터미널이나 명령 프롬프트 같은 것을 이용해 주세요.)

사용법은 간단합니다. 세가지 코드만 알면 됩니다.
```
import colorprinter as cp
cp.color()
cp.uncolor()
```
## color() 함수 사용법
예시 : color([글자 색:str], [배경색:str])

만약 색을 변경하지 않을 경우 none 을 넣으면 유지가 됩니다.
아래에 있는 색깔만 사용 가능합니다.
## black, red, green, yellow, blue, magenta, cyan, white
밝은 색을 원할경우 색 앞에 b를 넣으세요.

예시 : bblack, bgreen

## uncolor() 함수는 색을 원래대로 되돌립니다. 코드의 마지막에 넣어주시기 바랍니다.
예시 :
```
import colorprinter as cp

...

cp.uncolor()
```
또는
```
try:

  (대충 에러 날 수 있는 코드)
  
except:

  (무언가)
  
  cp.uncolor()
```
