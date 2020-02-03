"""
1) parameter 로 받은 string 의 양 끝단 2 글자를 붙여서 반환하는 함수
"""
def both_ends(s):
    if len(s) < 2:
        return ''
    first2 = s[:2]
    last2 = s[-2:]
    return first2 + last2

print(both_ends('spring'))
print(both_ends('Hello'))

"""
2) parameter 로 받은 string 의 선두 character 가 뒤따르는 문자열에 나타나면 * 로
    바꾸어 반환하는 함수
"""
def fix_starts(s):
    front = s[0]
    back = s[1:]
    fixed_back = back.replace(front, '*')
    return front + fixed_back

print(fix_starts('babble'))
print(fix_starts('google'))

"""
3) 두개의 문자열을 parameter 로 받아 서로의 첫번째 두 글자를 교환한 후 중간에 한칸
    띄우고 반환하는 함수
"""
def mix_up(a, b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return a_swapped + ' ' + b_swapped

mix_up('frog', 'dinner')

"""
4) 두개의 parameter 를 받아서 두개가 같으면 SAME 다르면 Different 를 반환하는 함수
"""
def test(got, expected):
    if got == expected:
        print('SAME')
    else:
        print('Different')

test('a', 'a')
test('aba', 'aca')
