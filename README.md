# cpuload

这个项目主要代码实现来自于`https://github.com/GaetanoCarlucci/CPULoadGenerator`

```bash

python CPULoadGenerator.py --core 8 --cpu_load 0.55 --min_freq 1.0GHz --max_freq 2.0GHz  --core 14 --cpu_load 0.12 --min_freq 2.4GHz --max_freq 2.5GHz  --duration 120


watch -n 1 cpupower -c 8,14 frequency-info

cpupower -c 8 frequency-set --min 1.0GHz --max 2.0GHz
```