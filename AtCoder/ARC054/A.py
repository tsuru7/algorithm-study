l, x, y, s, d = map(int, input().split())
speed = x + y
rspeed = y - x

distance = d - s if d >= s else l - s + d
rdistance = s - d if s >= d else s + l - d


elasped = distance / speed
if y > x:
    relasped = rdistance / rspeed
    if elasped < relasped:
        print(elasped)
    else:
        print(relasped)
else:
    print(elasped)
