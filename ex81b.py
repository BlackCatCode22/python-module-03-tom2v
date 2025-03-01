# Tong's Exercise 8.1b / Experiment
#

fh = open("mbox-short.txt")
for lx in fh:
    ly = lx.rstrip()
    wds = ly.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    email = wds[1].split("@")
    print(wds[1].upper())
    print("Host:", email[1].upper())