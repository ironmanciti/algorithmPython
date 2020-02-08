"""
1) 다음의 print 결과는 ?
"""
s = "Python is awesome"
print(s[1:3])
#%%
"""
2) 다음 영어 문장에서 너(you)는 몇번 나오는가 ?
    "You don't go to school on Saturday. I want you be happy.
    I miss you very much. You don't forget me"
"""
s = "You don't go to school on Saturday. I want you be happy. I miss you very much. You don't forget me"

s = s.lower()
print(s.count("you"))
#%%
"""
23 "Spam and Eggs" 를 입력할 때 다음 프로그램의 출력 결과는 ?
"""
def main():
    msg = input("Enter a phrase:  ")
    for w in msg.split():
        print(w[0], end="")

main()
#%%
"""
4) 다음의 출력 결과는 ?
"""
for x in "Mississippi".split("i"):
    print(x, end="")
#%%
"""
5) 다음 출력 결과는 ?
"""
s = "Jane Doe"
print(s[3 : 1 : -1])
#%%
"""
6) s = "Hello, Python World" 을 alphabet 별로 몇개인지 계산 (단, 대소문자 무시)
    * hint : 1. "," 와 " " 을 "" 로 replace
    2. s.lower() 를 이용하여 소문자로 통일
    3. dictionary 를 이용하여 알파벳 별 개수 누적
"""
s = "Hello, Python World"
s = s.replace(" ", "")
s = s.replace(",", "")
s = s.lower()
word_cnt = {}
for letter in s:
    if letter in word_cnt:
        word_cnt[letter] += 1
    else:
        word_cnt[letter] = 1

for k, v in sorted(word_cnt.items()):
    print(k, v)
#%%
"""
7) parameter 로 받은 string 의 선두 character 가 뒤따르는 문자열에 나타나면 * 로 바꾸어 반환하는 함수
"""
def fix_starts(s):
    front = s[0]
    back = s[1:]
    fixed_back = back.replace(front, '*')
    return front + fixed_back

print(fix_starts('babble'))
print(fix_starts('google'))