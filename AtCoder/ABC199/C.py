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
    s=input()
    q=i_input()
    tab = []
    for _ in range(q):
        tab.append(list(m_input()))
    return n,s,q,tab

def main(n,s,q,tab):
    s1 = list(s[:n])
    s2 = list(s[n:])
    # print(s1, s2)
    flip = False
    for t, a, b in tab:
        a = a-1
        b = b-1
        if t == 2:
            flip = not flip
        elif t == 1:
            if b < n:
                if flip == False:
                    s1[a], s1[b] = s1[b], s1[a]
                else:
                    s2[a], s2[b] = s2[b], s2[a]
            elif n <= a:
                a = a - n
                b = b - n
                if flip == False:
                    s2[a], s2[b] = s2[b], s2[a]
                else:
                    s1[a], s1[b] = s1[b], s1[a]
            else:
                b = b - n
                if flip == False:
                    s1[a], s2[b] = s2[b], s1[a]
                else:
                    s2[a], s1[b] = s1[b], s2[a]
        # print(s1,s2)
    if flip == False:
        ans = ''.join(s1) + ''.join(s2)
    else:
        ans = ''.join(s2) + ''.join(s1)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s,q,tab=readinput()
    ans=main(n,s,q,tab)
    printans(ans)
