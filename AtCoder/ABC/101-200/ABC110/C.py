from collections import deque
def readinput():
    s=input()
    t=input()
    return s,t

def main(s,t):
    tbl={}
    for i in range(len(t)):
        if t[i] == s[i]:
            if t[i] in tbl and tbl[t[i]] != t[i]:
                return 'No'
            else:        
                tbl[t[i]]=t[i]
        else:
            if t[i] in tbl and tbl[t[i]] != s[i]:
                return 'No'
            else:
                tbl[t[i]]=s[i]
            if s[i] in tbl and tbl[s[i]] != t[i]:
                return 'No'
            else:
                tbl[s[i]]=t[i]
    return 'Yes'

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    print(ans)
