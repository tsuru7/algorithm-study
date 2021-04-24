def readinput():
    s = input()
    return s

def main(s):
    if s[0] != 'A':
        return 'WA'
    # print(s)
    # print(s[2:-1])
    if s[2:-1].count('C') != 1:
        return 'WA'
    ls = s.lower()
    count = 0
    for i, c in enumerate(s):
        if c != ls[i]:
            count += 1
    if count != 2:
        return 'WA'
    else:
        return 'AC'

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
