def readinput():
    s=input()
    return s

def main(s):
    if s[-1]=='s':
        return s+'es'
    else:
        return s+'s'

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
