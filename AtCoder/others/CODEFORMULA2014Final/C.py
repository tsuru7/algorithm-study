def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s = input()
    return s

def get_username(s):
    i = 0
    name = ''
    username = False
    while i < len(s):
        if username and s[i] != '@' and s[i] != ' ':
            name += s[i]
        elif username and (s[i] == '@' or s[i] == ' '):
            return name, s[i:]
        elif s[i] == '@':
            username = True
        i += 1
    return name, ''

def main(s):
    names = set()
    remain = s
    while len(remain) > 0:
        name, remain = get_username(remain)
        if name != '':
            names.add(name)
        # print(names, remain)
    if len(names) > 0:
        return sorted(list(names))
    else:
        return []

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
