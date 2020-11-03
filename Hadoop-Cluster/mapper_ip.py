import sys
count = dict()

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    
    ip = words[0]
    count[ip] = count.get(ip, 0) + 1
    
    print '%s\t%s' % (ip, 1)
