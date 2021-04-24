from collections import deque
def readinput():
    s=input()
    t=input()
    return s,t

def main(s,t):
    table = [-1]*26
    for i in range(len(s)):
        print(table)
        cs = ord(s[i]) - ord('a')
        ct = ord(t[i]) - ord('a')
        print(cs, ct)
        if table[cs] == -1:
            table[cs] = ct
        elif table[cs] != ct:
            return 'No'
        if table[ct] == -1:
            table[ct] = cs
        elif table[ct] != cs:
            return 'No'
    return 'Yes'

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    print(ans)
