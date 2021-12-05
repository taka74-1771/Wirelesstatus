import psutil

while True:
    mem_us = psutil.virtual_memory()
    cpu_us = psutil.cpu_percent(interval=1)
    print("RAM_Use = " + str(mem_us.percent) + "%")
    print("CPU_Use = " + str(cpu_us) + "%")