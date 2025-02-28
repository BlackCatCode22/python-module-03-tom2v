# Tong's Exercise 7.1
#

fh = open("mbox-short.txt")
for lx in fh:
    ly = lx.rstrip()
    if ly.startswith("From "):
        print(ly.upper())
