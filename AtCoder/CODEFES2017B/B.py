from collections import Counter

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    d=l_input()
    m=i_input()
    t=l_input()
    return n,d,m,t

def main(n,d,m,t):
    counter_d = Counter(d)
    counter_t = Counter(t)
    for k,v in counter_t.items():
        if k in counter_d and counter_d[k] >= v:
            continue
        else:
            return 'NO'
    return 'YES'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d,m,t=readinput()
    ans=main(n,d,m,t)
    printans(ans)
