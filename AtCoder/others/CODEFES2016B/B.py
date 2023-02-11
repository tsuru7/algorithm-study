def readinput():
    n,a,b=list(map(int,input().split()))
    s=input()
    return n,a,b,s

def main(n,a,b,s):
    kokunai=0
    kaigai=0
    for c in s:
        if c=='a':
            if kokunai+kaigai<a+b:
                print('Yes')
                kokunai+=1
            else:
                print('No')
        elif c=='b':
            if kokunai+kaigai<a+b and kaigai<b:
                print('Yes')
                kaigai+=1
            else:
                print('No')
        else:
            print('No')

if __name__=='__main__':
    n,a,b,s=readinput()
    main(n,a,b,s)
