# cpuload

这个项目主要代码实现来自于`https://github.com/GaetanoCarlucci/CPULoadGenerator`

```bash
conda activate cpuload
python CPULoadGenerator.py --core 8 --cpu_load 0.15 --min_freq 0.8GHz --max_freq 1.0GHz  --core 9 --cpu_load 0.95 --min_freq 2.4GHz --max_freq 2.5GHz  --duration 120


watch -n 1 cpupower -c 8,14 frequency-info

cpupower -c 8 frequency-set --min 1.5GHz --max 2.0GHz
cpupower -c 14 frequency-set --min 2.4GHz --max 2.5GHz


python CPULoadGeneratorWithoutFreq.py ---core 48 --cpu_load 0.95  --duration 120
cpupower -c 48 frequency-set --freq 2.5GHz
cpupower -c 48 frequency-info
```

```text
(cpuload) root@cpuload:/workspace/cpuload# cpupower -c 48 frequency-set --freq 2.5GHz
modprobe: FATAL: Module msr not found in directory /lib/modules/5.4.0-144-generic
Setting cpu: 48
Error setting new values. Common errors:
- Do you have proper administration rights? (super-user?)
- Is the governor you requested available and modprobed?
- Trying to set an invalid policy?
- Trying to set a specific frequency, but userspace governor is not available,
   for example because of hardware which cannot be set to a specific frequency
   or because the userspace governor isn't loaded?
```