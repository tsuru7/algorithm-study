from math import pi

def readinput():
    oa, ab, bc = list(map(int,input().split()))
    return oa, ab, bc

def main(oa,ab,bc):
    if oa>ab+bc:
        s=pi*(oa+ab+bc)**2-pi*(oa-ab-bc)**2
    elif bc>oa+ab:
        s=pi*(oa+ab+bc)**2-pi*(bc-oa-ab)**2
    elif ab>oa+bc:
        s=pi*(oa+ab+bc)**2-pi*(ab-oa-bc)**2
    else:
        s=pi*(oa+ab+bc)**2
    return s

if __name__=='__main__':
    oa,ab,bc=readinput()
    ans=main(oa,ab,bc)
    print(ans)
