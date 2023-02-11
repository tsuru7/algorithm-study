def readinput():
    s=input()
    return s

def main(s):
    if s == 'AAA' or s == 'BBB':
        return 'No'
    else:
        return 'Yes'

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
