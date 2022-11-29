import re

def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('Not a match!')

pattern = r'is'
script = 'Life is so cool'
# refinder(pattern, script)

r = re.search(r'Life', script).group()
r = re.search(r'cool', script).group()
# 이렇게는 실행을 못한다.
# r = re.match(r'cool', script).group()
print(r)