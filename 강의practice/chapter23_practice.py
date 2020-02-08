# 이항계수
# 재귀적 구현
import time

def bino_coef(n, k):
    if k == 0 or n == k:
        return 1
    return bino_coef(n-1, k-1) + bino_coef(n-1, k)

stime = time.time()
print(bino_coef(30, 20))

etime = time.time()
print(etime-stime)

# memoization 기법 적용
#%%
def bino_coef_memo(n, k):
    cache = [[0 for _ in range(k+1)] for _ in range(n+1)]  #2차원배열

    for i in range(n+1):
        cache[i][0] = 1   # n개 중 하나도 안뽑는 경우의 수 = 1
    for i in range(k+1):
        cache[i][i] = 1   # k 개중 k 개를 뽑는 경우의 수 = 1

    for i in range(1, n+1):
        for j in range(1, k+1):
            cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
    return cache[n][k]

stime = time.time()
print(bino_coef_memo(30, 20))

etime = time.time()
print(etime-stime)