def readinput():
    s = input()
    return s

def main(s):
    if s[2] == s[3] and s[4] == s[5]:
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
