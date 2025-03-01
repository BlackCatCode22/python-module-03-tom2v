# Tong's Exercise 8.1
#

fh = open("mbox-short.txt")
for lx in fh:
    ly = lx.rstrip()
    wds = ly.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])