#!/usr/bin/python

from collections import Counter, defaultdict
from datetime import datetime

with open('input.txt', 'r') as f:
    data = f.read().rstrip('\n').splitlines()

guards = defaultdict(Counter)
for t, m in [l.split('] ') for l in sorted(data) if l]:
    t = datetime.strptime(t, '[%Y-%m-%d %H:%M')
    print(t)
    if 'Guard' in m:
        g = int(m.split('#')[1].split()[0])
        print(g)
    if 'asleep' in m:
        start = t
    if 'wakes' in m:
        minutes = int((t - start).total_seconds() // 60)
        guards[g].update(Counter((start.minute+i)%60 for i in range(minutes)))

_, guard_id = max((sum(c.values()), guard_id) for guard_id, c in guards.items())
print(guard_id * guards[guard_id].most_common()[0][0])
