def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,a,b,c,d=m_input()
    s=input()
    return n,a,b,c,d,s

def main(n,a,b,c,d,s):
    s = ' '+s
    for i in range(a+1, c-1):
        if s[i:i+2] == '##':
            # print('case1')
            return 'No'
    for i in range(b+1, d-1):
        if s[i:i+2] == '##':
            # print('case2')
            return 'No'
    if c < d:
        # print('case3')
        return 'Yes'
    for i in range(b-1, d):
        if s[i:i+3] == '...':
            # print('case4', i)
            return 'Yes'
    # print('case5')
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,c,d,s=readinput()
    ans=main(n,a,b,c,d,s)
    printans(ans)
