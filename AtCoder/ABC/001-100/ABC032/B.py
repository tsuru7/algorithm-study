def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s = input()
    k=i_input()
    return s,k

def main(s,k):
    pw = set()
    if k > len(s):
        return 0
    for i in range(len(s)-k+1):
        pw.add(s[i:i+k])
    return len(pw)

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,k=readinput()
    ans=main(s,k)
    printans(ans)
