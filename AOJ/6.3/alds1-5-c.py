from math import sqrt, sin, cos

def readinput():
    n=int(input())
    return n

def apex3(x1,y1,x2,y2):
    '''正三角形の残りの頂点(x3,y3)を求める
    
    1->2->3の順に反時計回り
    '''
    x3 = 1.0/2.0 *(x2-x1) -sqrt(3.0)/2.0 * (y2-y1) +x1
    y3 = sqrt(3.0)/2.0 * (x2-x1) + 1.0/2.0 * (y2-y1) +y1
    return x3,y3

def koch(x1,y1,x2,y2,l,lmax):
    #print('l:{}, lmax:{}'.format(l,lmax))
    if(l==lmax):
        return

    x3,y3=(x2-x1)/3 +x1, (y2-y1)/3 +y1
    x4,y4=(x2-x1)/3*2 +x1, (y2-y1)/3*2 +y1
    x5,y5 = apex3(x3,y3,x4,y4)

    koch(x1,y1,x3,y3,l+1,lmax)
    print('{:.10f} {:.10f}'.format(x3,y3))
    koch(x3,y3,x5,y5,l+1,lmax)
    print('{:.10f} {:.10f}'.format(x5,y5))
    koch(x5,y5,x4,y4,l+1,lmax)
    print('{:.10f} {:.10f}'.format(x4,y4))
    koch(x4,y4,x2,y2,l+1,lmax)

    return

def main(n):
    x0=0;y0=0
    x1=100;y1=0
    print('{:.10f} {:.10f}'.format(x0,y0))
    koch(x0,y0,x1,y1,0,n)
    print('{:.10f} {:.10f}'.format(x1,y1))


if __name__=='__main__':
    n=readinput()
    main(n)
