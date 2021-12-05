import psutil


while True:
    mem_us = psutil.virtual_memory()
    cpu_us = psutil.cpu_percent(interval=1)
    print(mem_us.percent)
    print(cpu_us)
