def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,k=m_input()
    return n,k

def get_points(x, n):
    if 2 <= x <= n:
        return x-1
    elif n < x <= 2*n:
        return 2*n+1-x
    else:
        return 0

def main(n,k):
    ans=0
    for y in range(2, 2*n+1):
        x = y + k
        if x > 2*n:
            continue

        ans += get_points(x, n) * get_points(y, n)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    printans(ans)
