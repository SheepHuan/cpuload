# cpuload

这个项目主要代码实现来自于`https://github.com/GaetanoCarlucci/CPULoadGenerator`

```bash
conda activate cpuload
python CPULoadGenerator.py --core 8 --cpu_load 0.15 --min_freq 0.8GHz --max_freq 1.0GHz  --core 9 --cpu_load 0.95 --min_freq 2.4GHz --max_freq 2.5GHz  --duration 120


watch -n 1 cpupower -c 8,14 frequency-info

cpupower -c 8 frequency-set --min 1.5GHz --max 2.0GHz
cpupower -c 14 frequency-set --min 2.4GHz --max 2.5GHz
```
