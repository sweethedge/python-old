# 특정 단어의 예문만 모아 파일로 저장하기 112p
import re

f = open('friends101.txt', 'r')
# 텍스트의 내용을 list로 만들려면 readlines()
sentences = f.readlines()

for i in sentences[:20]:
    if re.match(r'\w+:', i):
        print(i)

lines = [i for i in sentences if re.match(r'\w+:', i)]
lines[:10]

would = [i for i in sentences if re.match(r'\w+:', i) and re.search('would', i)]
take = [i for i in sentences if re.match(r'\w+:', i) and re.search('take', i)]
go = [i for i in sentences if re.match(r'\w+:', i) and re.search('go', i)]

# for i in take:
#     print(i)

newf = open('would.txt', 'w')
newf.writelines(would)
newf.close()