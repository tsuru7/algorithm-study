def readinput():
    s=input()
    return s

def main(s):
    terms=s.split('+')
    count=0
    for term in terms:
        if term.count('0') == 0:
            count+=1
    return count

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
