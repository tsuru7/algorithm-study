def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    s=input()
    return n,s

def main(n,s):
    count_w = [0]*n
    count_e = [0]*n
    for i in range(n):
        if s[i] == 'W':
            if i > 0:
                count_w[i] = count_w[i-1] + 1
            else:
                count_w[i] = 1
        else:
            if i > 0:
                count_w[i] = count_w[i-1]
    for i in range(n-1, -1, -1):
        if s[i] == 'E':
            if i < n-1:
                count_e[i] = count_e[i+1] + 1
            else:
                count_e[i] = 1
        else:
            if i < n-1:
                count_e[i] = count_e[i+1]
    mincount = count_e[1]
    for i in range(1, n-1):
        mincount = min(mincount, count_w[i-1]+count_e[i+1])
    mincount = min(mincount, count_w[n-2])
    return mincount

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    printans(ans)
