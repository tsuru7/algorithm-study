def readinput():
    '''グラフを読み込む

    Returns
    --------------------------------
    n: int
        頂点の数
    nList: list
        隣接リスト nList[u]はノード u の隣接リスト
        それぞれのノードに対するリストの最後に -1 を番兵として追加してある
    '''

    n = int(input())

    # 隣接リストの初期化
    nList = []
    # 1-originにするためn+1個の空リストをappend
    for _ in range(n+1):
        nList.append([])

    # 隣接リストの読み込み
    for _ in range(n):
        l = list(map(int, input().split()))
        u = l[0]
        k = l[1]
        for i in range(k):
            nList[u].append(l[i+2])
        nList[u].append(-1) # 番兵

    return n, nList

# 定数定義
WHITE = 0
GRAY = 1
BLACK = 2

def dfs(u, nList):
    '''グラフを深さ優先探索でたどり、各頂点の発見時刻、操作完了時刻を更新する

    Parameters:
    -----------------
    u: int
        始点 (1-origin)
    nList: list
        隣接リスト (1-origin)

 
    '''
    global ts_find
    global ts_comp
    global status
    global time_

    # print(f'dfs({u})')

    status[u] = GRAY
    time_ += 1
    ts_find[u] = time_

    for v in nList[u]:
        if v != -1:
            if status[v] == WHITE:
                dfs(v, nList)
        else:
            # 各頂点に関する操作はここで実施
            status[u] = BLACK
            time_ += 1
            ts_comp[u] = time_
    
        

if __name__ == '__main__':
    n, nList = readinput()
    ts_find = [0] * (n+1)
    ts_comp = [0] * (n+1)
    status = [WHITE] * (n+1)
    time_ = 0

    for u in range(1, n+1):
        if status[u] == WHITE:
            dfs(u, nList)

    for i in range(1, n+1):
        print('{} {} {}'.format(i, ts_find[i], ts_comp[i]))


