import sys
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    slist = []
    for _ in range(n):
        slist.append(input())
    return n,slist

def main(n,slist):
    total_count = [INFTY]*26
    for i in range(n):
        count = [0]*26
        for j in range(len(slist[i])):
            c = ord(slist[i][j]) - ord('a')
            count[c] += 1
        for j in range(26):
            total_count[j] = min(total_count[j], count[j])
    ans=''
    for i in range(26):
        ans += chr(ord('a')+i)*total_count[i]

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,slist=readinput()
    ans=main(n,slist)
    printans(ans)
