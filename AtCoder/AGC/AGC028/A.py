from math import gcd

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n, m = m_input()
    s = input()
    t = input()
    return n,m,s,t

def main(n,m,s,t):
    ans = n*m//gcd(n, m)
    x = {}
    times = ans//n
    for i in range(n):
        x[i*times] = s[i]
    times = ans//m
    for i in range(m):
        if i*times in x and x[i*times] != t[i]:
            return -1
    return ans


def printans(ans):
    print(ans)

def randominput():
    from random import choice, randint
    n = randint(1, 1000)
    s = ''
    for i in range(n):
        s += choice('abcdefghijklmnopqrstuvwxyz')
    m = randint(1, 1000)
    t = ''
    for i in range(m):
        t += choice('abcdefghijklmnopqrstuvwxyz')
    return n, m, s, t

if __name__=='__main__':
    n,m,s,t=readinput()
    # for i in range(10000):
    #     n,m,s,t=randominput()
    #     print(n, m)
    #     print(s)
    #     print(t)
    ans=main(n,m,s,t)
    printans(ans)
