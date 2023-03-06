"""
Goal: cleanly simulate X seconds of runtime.
Runs X machines and then logs results.
"""

import random
from machine import Machine
import time
import copy
import time
import sys

EXECUTION_TIME = 60
NUM_MACHINES = 3

logfiles = [f"l{i}.txt" for i in range(NUM_MACHINES)]

rand_port = random.randint(8000, 28000)
ports = [rand_port+i for i in range(NUM_MACHINES)]
hosts = ['localhost' for i in range(NUM_MACHINES)]

print(f"Initializing machines on ports {ports}.")
machines = [Machine(interactive=False) for i in range(NUM_MACHINES)]
for i in range(len(machines)):
    machines[i].start(ports[i], logfiles[i])

print("Adding ports.")
for i in range(len(machines)):
    ports_copy = copy.deepcopy(ports)
    hosts_copy = copy.deepcopy(hosts)
    ports_copy.pop(i)
    hosts_copy.pop(i)
    machines[i].add_nonint_connections(hosts_copy, ports_copy)

print("Running machines.")

# Progress Bar

sys.stdout.write("[%s]" % (" " * EXECUTION_TIME))
sys.stdout.flush()
sys.stdout.write("\b" * (EXECUTION_TIME+1)) # return to start of line, after '['

for i in range(EXECUTION_TIME): # 1 tick per second
    time.sleep(1)
    sys.stdout.write("-")
    sys.stdout.flush()

# Kill Threads to stop sending/receiving
for m in machines:
    m.kill_flag.set()

print(f"Done simulating for {EXECUTION_TIME} seconds. Quit out now.")







