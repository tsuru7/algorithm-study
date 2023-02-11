def readinput():
    s=input()
    t=input()
    return s,t

def main(s,t):
    if s == 'Y':
        return t.upper()
    else:
        return t

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    print(ans)
