import re

number = 'My number is 511223-1****** and yours is 521012-2******'
sentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
data = 'a:3; b:4; c:5'
words = 'I am home now. \n\n\nI am with my cat. \n\n'
sentencely = 'I have a lovely dog, really. I am not telling a lie.'

# findall
# p = re.findall('\d{6}', number)
# print(p)

# findall + greedycontrol
# example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'
# r = re.findall(r'\d.+?년', example1)
# print(r)

# split 95p - 문자열 나누기
p2 = re.split(r'[.?!]', sentence)
print(p2)

# for i in re.split(r'; ', data):
#     print(re.split(':', i))

# sub 97p -- 문자열 바꾸기
# words2 = (re.sub(r'\n', '', words))
# print(words2)
# words3 = re.sub(r'cat', 'dog', words2)
# print(words3)

# words4 = re.findall(r'\w+ly', sentencely)
# print(words4)