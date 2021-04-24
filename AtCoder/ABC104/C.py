def readinput():
    d,g=map(int,input().split())
    pc=[]
    for _ in range(d):
        pc.append(list(map(int,input().split())))
    return d,g,pc

def main(d,g,pc):

    dpでやらないとダメぽいね

    # i = d - 1
    # count = 0
    # while g>0:
    #     if pc[i][0] * (i + 1) * 100 + pc[i][1] < g:
    #         count += pc[i][0]
    #         g -= (pc[i][0] * (i + 1) * 100 + pc[i][1]) # complete
    #     elif pc[i][0] * (i + 1) * 100 < g <= pc[i][0] * (i + 1) * 100 + pc[i][1]:
    #         count += pc[i][0]
    #         return count
    #     else:
    #         count += g // (pc[i][0] * (i + 1) * 100)
    #         if g % (pc[i][0] * (i + 1) * 100) != 0:
    #             count += 1
    #         return count

if __name__=='__main__':
    d,g,pc=readinput()
    ans=main(d,g,pc)
    print(ans)
