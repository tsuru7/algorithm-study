def readinput():
    n,m=list(map(int,input().split()))
    prefs=[]
    for _ in range(n+1):
        prefs.append([])
    for i in range(1,m+1):
        pi,yi=list(map(int,input().split()))
        prefs[pi].append([i,yi])
    return n,m,prefs

def main(n,m,prefs):
    citycodes=['000000000000']*(m+1)
    for i in range(1,n+1):
        pref=prefs[i]
        pref.sort(key=lambda x:x[1])
        prefcode='{:06}'.format(i)
        #print(pref, prefcode)
        for j, city in enumerate(pref):
            citycode='{:06}'.format(j+1)
            #print(city, citycode)
            citycodes[city[0]]=prefcode+citycode
    return citycodes

if __name__=='__main__':
    n,m,prefs=readinput()
    citycodes=main(n,m,prefs)
    for i in range(1,m+1):
        print(citycodes[i])
    
