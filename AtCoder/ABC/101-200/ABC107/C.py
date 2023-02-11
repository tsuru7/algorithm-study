from bisect import bisect_left
import sys
INFTY = sys.maxsize

def readinput():
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    return n,k,x

def main(n,k,x):
    zero_i = bisect_left(x, 0)
    # print(f'zero_i: {zero_i}')
    if zero_i >= len(x):
        left = x
        right = []
    elif x[zero_i] == 0:
        left = x[:zero_i]
        right = x[zero_i+1:]
        k -= 1
    else:
        left = x[:zero_i]
        right = x[zero_i:]
    
    left = sorted([-x for x in left])
    # print(left, right, k)

    if k == 0:
        return 0

    # s_left = [0] * len(left)
    # s_right = [0] * len(right)

    # s_left[0] = abs(left[-1])
    # for i in range(1, len(left)):
    #     s_left[i] = s_left[i-1] + abs(left[-i-1])
    # s_right[0] = right[0]
    # for i in range(1, len(right)):
    #     s_right[i] = s_right[i-1] + right[i]

    tmin = INFTY

    # 折り返しなし（右側のみ点灯）の場合
    if k <= len(right):
        tmin = min(tmin, right[k-1])
        # print('tmin: {}, right_i: {}'.format(tmin, k-1))

    # 折り返し無し（左側のみ点灯）の場合
    if k <= len(left):
        tmin = min(tmin, abs(left[k-1]))
        # print('tmin: {}, left_i: {}'.format(tmin, k-1))

    if len(right) > 0 and len(left) > 0:

        # 左側で折り返しの場合
        left_i = 0
        while left_i < len(left):
            right_i = k - left_i - 2
            if 0 <= right_i < len(right):
                tmin = min(tmin, right[right_i] + left[left_i]*2)
                # print('tmin: {}, left_i: {}, right_i: {}'.format(tmin, left_i, right_i))
            left_i += 1
            right_i -= 1


        # 右側で折り返しの場合

        right_i = 0
        while right_i < len(right):
            left_i = k - right_i - 2
            if 0 <= left_i < len(left):
                tmin = min(tmin, right[right_i]*2 + abs(left[left_i]))
                # print('tmin: {}, left_i: {}, right_i: {}'.format(tmin, left_i, right_i))
            right_i += 1
            left_i -= 1

    return tmin

if __name__=='__main__':
    n,k,x=readinput()
    ans=main(n,k,x)
    print(ans)
