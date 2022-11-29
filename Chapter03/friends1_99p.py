import re

# 읽은 걸 script101에 대입한다
f = open('friends101.txt', 'r', encoding="utf8")
script101 = f.read()
# print(script101[:100])

# script101에 Monica:로 시작하는 거를 찾아서 Line에 대입한다
Line = re.findall(r'Monica:.+', script101)

# Line의 요소 3개만 읽어서 프린트
    # for i in Line[:3]:
    #     print(i)

# 문자열 변수를 하나 선언하고
    # monica = ''

# Line의 길이만큼 i를 키우면서 monica에 대입. 엔터도 넣어준다
    # for i in Line:
    #     monica += i + '\n'

# 그 monica를 쓰고
    # f.write(monica)
# 문닫기
    # f.close()

# 특정 등장인물의 대사만 출력하기
# 정규표현식을 반환받고 싶을 때는 re.compile()
#     char = re.compile(r'[A-Za-z]+:')
# 그걸 텍스트에서 찾고 싶을 때는 re.findall()
#     p1 = re.findall(char, script101)
# 중복을 제거하고 싶을 때는 set()
#     p2 = set(re.findall(char, script101))
# 문자열을 배열에 넣고 싶을 때는 list()를 써서 list로 변환
#     listp2 = list(p2)
# 배열을 만들고
#     character = []

# 반복문으로 대입한 뒤
#     for i in listp2:
#         character += [i[:-1]]

# 출력
#     print(character)

# 한 줄 요약은 다음과 같다.
# character2 = [x[:-1] for x in list(set(re.findall(r'[A-Za-z]+:', script101)))]
# print(character2)

# 지문만 출력하기
re.findall(r'\(\w.+\)', script101)[:6]

# for i in listName:
# for (int i = 0; i < listname.length; i++) {
