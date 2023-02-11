def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n, m, q = m_input()
    wvList = []
    for _ in range(n):
        w, v = m_input()
        wvList.append((v,w))
    xList=l_input()
    query = []
    for _ in range(q):
        query.append(l_input())
    return n,m,q,wvList,xList,query

def main(n,m,q,wvList,xList,query):
    ans = []
    wvList = sorted(wvList, reverse=True, key=lambda x:x[0])
    # print(wvList)
    for l, r in query:
        # print(l-1, r)
        if r == len(xList):
            xList2 = sorted(xList[:l-1])
        else:
            xList2 = sorted(xList[:l-1]+xList[r:])
        # print(xList2)
        value = 0
        used = [0]*n
        for x in xList2:
            for i in range(n):
                if wvList[i][1] <= x and used[i] == 0:
                    used[i] = 1
                    value += wvList[i][0]
                    break
        # print(used)
        ans.append(value)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,m,q,wvList,xList,query=readinput()
    ans=main(n,m,q,wvList,xList,query)
    printans(ans)
