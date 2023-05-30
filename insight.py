import psutil
import re
import time
import os


core = [50,52]
wnt_util = [0.15,0.95] 
wnt_freq = [('0.9GHz','1.0GHz'),('2.4GHz','2.5GHz')]
d = 120

def get_cur_freq(cpus):
    cpu_num = [str(c) for c in cpus]
    cpu_num =','.join(cpu_num)
    cmd = f'cpupower -c {cpu_num} frequency-info'
    res = os.popen(cmd)
    text = res.read()
    # print(text)
    match = re.findall(r'current CPU frequency: (\d+\.\d+ .*Hz) ', text)

    freq = []
    for item in match:
        r = re.search(r'\d+\.\d+', item)
        float_num = float(r.group())
        if 'M' in item:
            float_num = float_num / 10e3
        elif 'K' in item:
            float_num = float_num / 10e6
        # print(item,float_num)
        freq.append(float_num)

    return freq

data = {}
cmd = 'python CPULoadGenerator.py '
for idx,c in enumerate(core):
    cmd += f'--core {c} --cpu_load {wnt_util[idx]} --min_freq {wnt_freq[idx][0]} --max_freq {wnt_freq[idx][1]} '
    data[c] = {
        'idx': [],
        'freq': [],
        'util':[]
    }
cmd += f'--duration {d}'
# res = os.popen(cmd)

print(cmd)
s = time.time()
for i in range(1000):
    e = time.time()
    if e - s > d +15:
        break
    real_util = psutil.cpu_percent(interval=0.5, percpu=True)
    print(len(real_util))
    real_freq = get_cur_freq(core)
    for idx,c in enumerate(core):
        try:
            print(c,int(e-s),real_util[c],real_freq[idx])
            
            data[c]['idx'].append(int(e-s))
            data[c]['freq'].append(real_freq[idx])
            data[c]['util'].append(real_util[c])
        except:
            pass
    time.sleep(0.8)

import json
data['core'] = core
data['wnt_util'] = wnt_util
data['wnt_freq'] = wnt_freq
open("insight.json",'w').write(json.dumps(data,indent=4,ensure_ascii=False))

