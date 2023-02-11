def readinput():
    n,c=map(int,input().split())
    aList = []
    bList = []
    for i in range(n):
        ai,bi,ci=map(int,input().split())
        aList.append([ai, ci])
        bList.append([bi, -ci])
    return n,c,aList,bList

def main(n,c,aList,bList):
    aList.sort()
    bList.sort()
    aList2 = []
    bList2 = []
    aList2.append(aList[0])
    bList2.append(bList[0])
    for i in range(1, n):
        if aList[i][0] == aList2[-1][0]:
            aList2[-1][1] += aList[i][1]
        else:
            aList2.append(aList[i])
        if bList[i][0] == bList2[-1][0]:
            bList2[-1][1] -= bList[i][1]
        else:
            bList2.append(bList[i])
    
    ia = 0
    ib = 0
    prime = False
    totalcost = 0
    daycost = aList2[ia][1]    # １日当たりのコスト
    prevday = aList2[ia][0]     # 前回コスト計算した日
    ia += 1
    while True:
        if ia < len(aList2) and ib < len(bList2):
            if aList2[ia][0] < bList2[ib][0]:
                today = aList2[ia][0]
                if prime:
                    totalcost += (today - prevday)*c       # 前日までのトータルコストを計算 (prime)
                else:
                    totalcost += (today - prevday)*daycost  # 前日までのトータルコストを計算

                daycost += aList2[ia][1] # 今日からの１日当たりのコスト
                if daycost >= c:
                    prime = True
                ia += 1
                prevday = today

            elif aList2[ia][0] > bList2[ib][0]:
                today = bList2[ib][0]
                if prime:
                    totalcost += (today - prevday + 1)*c
                else:
                    totalcost += (today - prevday + 1)*daycost
                daycost += bList2[ib][1]
                if daycost < c:
                    prime = False
                ib += 1
                prevday = today+1

            elif aList2[ia][0] == bList2[ib][0]:
                today = aList2[ia][0]
                if prime:
                    totalcost += (today - prevday)*c       # 前日までのトータルコストを計算 (prime)
                else:
                    totalcost += (today - prevday)*daycost  # 前日までのトータルコストを計算

                daycost += aList2[ia][1] # 今日からの１日当たりのコスト
                if daycost >= c:
                    prime = True

                # 今日の分のコストを加算
                if prime:
                    totalcost += c
                else:
                    totalcost += daycost

                daycost += bList2[ib][1]
                if daycost < c:
                    prime = False
                ia += 1
                ib += 1
                prevday = today+1

        elif ib < len(bList2):
            today = bList2[ib][0]
            if prime:
                totalcost += (today - prevday + 1)*c
            else:
                totalcost += (today - prevday + 1)*daycost
            daycost += bList2[ib][1]
            if daycost < c:
                prime = False
            ib += 1
            prevday = today+1

        else:
            break
    return totalcost

if __name__=='__main__':
    n,c,aList,bList=readinput()
    ans=main(n,c,aList,bList)
    print(ans)
