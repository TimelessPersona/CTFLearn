f = open("data.dat", "r")

lines = f.readlines()
cnt = 0
for i in lines:
    if i.count("0")%3==0:
        cnt += 1
    if i.count("1")%2==0:
        cnt += 1
    if i.count("1")%2==0 and i.count("0")%3==0:
        cnt -= 1
print(cnt)
    #cnt = 0