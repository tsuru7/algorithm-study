import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    n,k=m_input()
    a=l_input()
    return n,k,a

def main(n,k,a):
    a.sort(reverse=True)
    a.append(0)

    # print(f'a: {a}')

    ans = 0
    for i in range(n):
        # print(f'k: {k}, ans: {ans}')
        a1 = a[i]
        a2 = a[i+1]
        max_count = (a1-a2)*(i+1)
        # print(f'a1: {a1}, a2:{a2}, max_count: {max_count}')
        if max_count <= k:
            ans += ((a1+a2+1)*(a1-a2)//2)*(i+1)
            k -= max_count
        else:
            full_count = k // (i+1)
            residue = k % (i+1)
            a2 = a1 - full_count
            ans += ((a1+a2+1)*(a1-a2)//2)*(i+1)
            ans += a2 * residue
            break

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    printans(ans)
