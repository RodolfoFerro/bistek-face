import os
import psutil

# Get current Process ID:
pid = os.getpid()


def get_memory_status(pid):
    # Build psutil process from PID:
    p = psutil.Process(pid)
    print("Process ID:", pid)

    # Print memory status:
    mem_usage = p.memory_percent()
    print("Memory: {:.4f}%".format(mem_usage))
    print()


consume_memory = range(20*1000*1000)

while True:
    get_memory_status(pid)
