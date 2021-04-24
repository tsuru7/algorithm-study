def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    flowers = []
    for _ in range(n):
        flowers.append(i_input())
    return n,flowers

def main(n,flowers):
    visited = [False]*(10**5 + 1)
    jufun = 0
    for i in range(n):
        now = flowers[i]
        if visited[now] == False:
            visited[now] = True
        else:
            jufun += 1
    return jufun

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,flowers=readinput()
    ans=main(n,flowers)
    printans(ans)
