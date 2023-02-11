import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    n=i_input()
    sList = [input() for _ in range(n)]
    return n,sList

def makeHashLists(sList, mod):
    n = len(sList)
    hashLists = [[] for _ in range(n)]
    for i in range(n):
        si = sList[i]
        hash = 0
        for j in range(len(si)):
            hash *= 100
            hash += ord(si[j]) - ord('a') + 1
            hash %= mod
            hashLists[i].append(hash)
    return hashLists

def getLCP(sList, mod):
    hashLists = makeHashLists(sList, mod)
    matchDict = dict()
    for i in range(n):
        for j in range(len(hashLists[i])):
            x = hashLists[i][j]
            if x not in matchDict:
                matchDict[x] = 1
            else:
                matchDict[x] += 1
    # print(matchDict)
    ans=[]
    for i in range(n):
        lcp = 0
        for j in range(len(hashLists[i])):
            x = hashLists[i][j]
            if matchDict[x] > 1:
                lcp = max(lcp, j+1)
            elif matchDict[x] == 1:
                break
        ans.append(lcp)
    return ans


def solve(n,sList):
    # 全文字列の長さの合計が5*10**5程度ということは10**11回程度の比較をすることになる
    # https://snuke.hatenablog.com/entry/2017/02/03/035524 よりMODとして10**18程度であれば問題無さそう
    # MOD1 = 999999797
    # MOD2 = 1000000007
    # MOD3 = 1000000009
    MOD4 = 1000000000000000003
    # lcp1 = getLCP(sList, MOD1)
    # lcp2 = getLCP(sList, MOD2)
    # lcp3 = getLCP(sList, MOD3)
    # ans = [min(x, y, z) for x, y, z in zip(lcp1, lcp2, lcp3)]
    lcp4 = getLCP(sList, MOD4)
    return lcp4

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,sList=readinput()
    ans=solve(n,sList)
    printans(ans)
