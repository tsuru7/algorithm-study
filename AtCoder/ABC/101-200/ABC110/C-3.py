from collections import deque
def readinput():
    s=input()
    t=input()
    return s,t

def main(s,t):
    table_to = [-1]*26
    table_from = [-1]*26
    for i in range(len(s)):
        cs = ord(s[i]) - ord('a')
        ct = ord(t[i]) - ord('a')
        if table_to[cs] == -1:
            table_to[cs] = ct
        else:
            if table_to[cs] != ct:
                return 'No'
        if table_from[ct] == -1:
            table_from[ct] = cs
        else:
            if table_from[ct] != cs:
                return 'No'
    return 'Yes'

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    print(ans)
