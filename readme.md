# Colorprinter
파이썬에서 print() 에 색을 쉽게 지정하세요!

(주의, 파이썬 기본으로 내장되어있는 idle 에서 작동하지 않습니다, 터미널이나 명령 프롬프트 같은 것을 이용해 주세요.)

사용법은 간단합니다. 두 줄의 코드만 기억하시면 됩니다.
```python
import colorprinter as cp
cp.colorprint("Sample Text", "black", "white")
```
만약 색을 변경하지 않을 경우 none 을 넣으면 유지가 됩니다.
## 사용 가능한 색 목록
* black, red, green, yellow, blue, magenta, cyan, white
* 밝은 색을 원할경우 색 앞에 b를 넣으세요.
`예시 : bblack, bgreen`
