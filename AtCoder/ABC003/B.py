def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s = input()
    t = input()
    return s, t

def main(s, t):
    for i in range(len(s)):
        if s[i] == t[i]:
            continue

        if s[i] == '@':
            if t[i] == '@':
                continue
            elif t[i] in 'atcoder':
                continue
            else:
                # print(s[i], t[i])
                return 'You will lose'
        elif s[i] in 'atcoder' and t[i] == '@':
            continue
        else:
            # print('case1',s[i],t[i])
            return 'You will lose'
    return 'You can win'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s, t=readinput()
    ans=main(s, t)
    printans(ans)
