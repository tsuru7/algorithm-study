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
    n,k=m_input()
    a=[]
    for _ in range(n):
        a.append(i_input())
    return n,k,a

def find_increasing(b, n, k, i):
    jstart = i
    inc_count = 1
    j = jstart
    while j+1 < n:
        # print(f'j: {j}, inc_count: {inc_count}')
        if b[j+1] > 0:
            inc_count += 1
            if inc_count == k:
                return jstart
        else:
            inc_count = 1
            jstart = j + 1
        j += 1
    return -1

def main(n,k,a):
    if k == 1:
        return n
    
    b = [0]*n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = a[i] - a[i-1]
    # print(b)
    j = find_increasing(b, n, k, 0)
    # print(f'find_increasing={j}')
    if j == -1:
        return 0
    ans = 1
    while True:
        # print(f'j={j}')
        if j+k>=n:
            return ans
        elif b[j+k] > 0:
            ans += 1
            j += 1
        else:
            j = find_increasing(b, n, k, j+1)
            # print(f'find_increasing={j}')
            if j == -1:
                return ans
            else:
                ans += 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    printans(ans)
