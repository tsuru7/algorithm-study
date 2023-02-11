from math import sqrt
from decimal import *

def readinput():
    x, y, r=input().split()
    return Decimal(x), Decimal(y), Decimal(r)

def dist2(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


def main(x, y, r):
    
    count = 0
    x0 = int( (x-r).to_integral_value() )
    x1 = int( (x+r).to_integral_value() )
    # print(f'x0: {x0}, x1: {x1}')
    for xx in range(x0-1, x1+2):
        # print(f'xx: {xx}')
        if r**2 - (xx - x)**2 < 0:
            continue
        y1 = ( y + (r**2 - (xx - x)**2).sqrt() ).to_integral_value(rounding=ROUND_FLOOR)
        y2 = ( y - (r**2 - (xx - x)**2).sqrt() ).to_integral_value(rounding=ROUND_CEILING)

        # print(xx, y1, y2, floor10000(y1), ceil10000(y2))

        count += y1 - y2 + 1

    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    x, y, r=readinput()
    ans=main(x, y, r)
    printans(ans)
