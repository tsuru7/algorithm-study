def readinput():
    s=input()
    t=input()
    return s,t

def main(s,t):
    if(len(t)==len(s)+1):
        if(t[0:len(t)-1]==s):
            return True
        else:
            return False
    else:
        return False
    

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    if(ans==True):
        print('Yes')
    else:
        print('No')