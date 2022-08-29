import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    b=l_input()
    c=l_input()
    return n,a,b,c

def main(n,a,b,c):
    a.sort()
    b.sort()
    c.sort()
    # print(f'a: {a}')
    # print(f'b: {b}')
    # print(f'c: {c}')

    # count_a[i]: Biを選んだときに作れるパターン数
    count_a = [0]*n
    j = 0
    for i in range(n):
        while j < n and b[i] > a[j]:
            j += 1
        count_a[i] = j
    # print(f'count_a: {count_a}')
    
    # count_ab[i]: B0からBiまでで作れるABのパターン数
    count_ab = [0]*n
    count_ab[0] = count_a[0]
    for i in range(1, n):
        count_ab[i] = count_ab[i-1]+count_a[i]
    # print(f'count_ab: {count_ab}')

    count_b = [0]*n
    j = 0
    for i in range(n):
        while j < n and c[i] > b[j]:
            j += 1
        count_b[i] = j
    # print(f'count_b: {count_b}')

    ans = 0
    for i in range(n):
        if count_b[i] == 0:
            continue
        ans += count_ab[count_b[i]-1]
        # print(f'i: {i}, ans: {ans}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,c=readinput()
    ans=main(n,a,b,c)
    printans(ans)
