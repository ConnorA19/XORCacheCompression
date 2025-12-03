"""
A simple gem5 configuration script to demonstrate FPC cache compression.
This sets up a basic system with an L1 data cache using FPC compression.
Runs a hello world program.
"""

import m5
from m5.objects import *

# Define a basic L1 cache class
class L1Cache(Cache):
    assoc = 4
    tag_latency = 1
    data_latency = 1
    response_latency = 1
    mshrs = 8
    tgts_per_mshr = 16
    size = '32kB'

    def connectCPU(self, cpu):
        raise NotImplementedError

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports

class L1DCache(L1Cache):
    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port

# Create the system
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '2GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('256MB')]

# Create a CPU
system.cpu = TimingSimpleCPU()

# Create the L1 data cache with FPC compression
l1d = L1DCache()
l1d.compressor = FPCDCompressor()
l1d.tags = CompressedTags()
l1d.tags.compressor = l1d.compressor
l1d.tags.block_size = 64
l1d.tags.max_compression_ratio = 2  # Allow compression
system.cpu.dcache = l1d

# Connect cache to CPU and bus
system.membus = SystemXBar()
l1d.connectCPU(system.cpu)
l1d.connectBus(system.membus)

# Memory controller
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_2133_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# Interrupt controller
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_master = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_slave = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

# Process for hello world
process = Process()
process.cmd = ['tests/test-progs/hello/bin/x86/linux/hello']
system.cpu.workload = process
system.cpu.createThreads()

# Instantiate and simulate
root = Root(full_system=False, system=system)
m5.instantiate()

print("Starting simulation...")
exit_event = m5.simulate()
print(f"Simulation ended at tick {m5.curTick()} due to {exit_event.getCause()}")