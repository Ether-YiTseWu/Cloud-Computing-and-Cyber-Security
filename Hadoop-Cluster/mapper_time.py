import sys
count = dict()

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    time = words[3][1:15] + ":00:00"

    print '%s\t%s' % (time, 1)
