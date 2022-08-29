def readinput():
    ant = []
    for _ in range(5):
        ant.append(int(input()))
    k=int(input())
    return ant,k

def main(ant,k):
    for i in range(4):
        for j in range(i+1,5):
            if ant[j] - ant[i] > k:
                return ':('
            else:
                continue
    return 'Yay!'

if __name__=='__main__':
    ant,k=readinput()
    ans=main(ant,k)
    print(ans)
