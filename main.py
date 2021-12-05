import psutil

while True:
    mem_us = psutil.virtual_memory()
    cpu_us = psutil.cpu_percent(interval=1)
    print("\rRAM_Use = " + str(mem_us.percent) + "%", flush=True)
    print("CPU_Use = " + str(cpu_us) + "%" + "\033[1A", end='', flush=True)

    #print(type(mem_us))
    #print(type(cpu_us))