n=int(input())
tree={}
for i in range(1, n):
    a, b = list(map(int,input().split()))
    if a in tree.keys:
        tree[a].append(b)
    else:
        tree[a]=list(b)

# rootノードを探す
for k in tree.keys:
    found=False
    for j in tree.keys:
        if (j==k):
            continue
        if k in tree[j]:
            found=True
            break
    if(not found):
        tree[k].append(0)
        break

nchild=[]
for k in tree.keys:
    nchild.append(len(tree[k]))

nchild.sort(reverse=True)
print(nchild[0])

