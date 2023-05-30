import matplotlib.pyplot as plt
import numpy as np
import json

data = json.loads(open("insight.json","r").read())
lns = []
color = [
    'red',
    'blue',
    'green',
    'navy',
]
def generate_random_color():
    r = np.random.random()
    g = np.random.random()
    b = np.random.random()
    return (r, g, b)


fig, ax1 = plt.subplots()
fig.set_size_inches(10, 8)
ax1.set_xlabel('time ')
ax1.set_ylabel('frequency (GHz)')
ax2 = ax1.twinx()
ax2.set_ylabel('utilization (%)')

s,e = 0,50
for idx,key in enumerate(['48','52']):
    # if not isinstance(key,int):
    #     print(key,key.type)
    #     continue
    ln1 ,= ax1.plot(data[key]['idx'][s:e],  data[key]['freq'][s:e], label=f'{key}_freq', linestyle = '-',marker='o',color=color[idx*2])
    ln2 ,= ax2.plot(data[key]['idx'][s:e],  data[key]['util'][s:e], label=f'{key}_util', linestyle = '--',marker='^',color=color[idx*2+1])
    lns.append(ln1)
    lns.append(ln2)

labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=4)

plt.savefig("t.png")