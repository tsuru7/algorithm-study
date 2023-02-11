def readinput():
    s=input()
    return s

def main(s):
    if 'A' <= s and s <='Z':
        return 'A'
    elif 'a' <= s and s <= 'z':
        return 'a' 
    return ''

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
