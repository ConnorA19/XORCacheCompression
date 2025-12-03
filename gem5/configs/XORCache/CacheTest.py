"""
Configuration file to test FPC cache compression on both L1D and L1I caches
in gem5 v25.1+. Uses class attributes to ensure correct CompressedTags initialization.
"""

import os
import m5
from m5.objects import *
from m5.objects import Cache, Compressors, CompressedTags
from m5.objects import X86TimingSimpleCPU, SystemXBar, MemCtrl, DDR3_1600_8x8
from m5.util import addToPath
m5.util.addToPath('../')
from common import SimpleOpts

# Add the common scripts to our path (assuming run from configs/example/...)


# --- 1. Custom Cache Definitions with FPC Compression ---

# Base parameters common to both L1 caches
L1_ASSOC = 4
L1_SIZE = '2KiB'
L1_LATENCY = 1
L1_MSHRS = 8
L1_TGTS = 16

class CompressedL1Cache(Cache):
    """
    Base class for L1 Caches using CompressedTags with FPC.
    Defines 'tags' as a class attribute for robust initialization.
    """
    assoc = L1_ASSOC
    tag_latency = L1_LATENCY
    data_latency = L1_LATENCY
    response_latency = L1_LATENCY
    mshrs = L1_MSHRS
    tgts_per_mshr = L1_TGTS
    size = L1_SIZE
    
    # 🌟 FIX: Define tags as a class attribute to ensure correct initialization.
    tags = CompressedTags(
        compressor = Compressors.FPCD(),
        block_size = 64, # Default cache line size
        max_compression_ratio = 2,
        num_blocks_per_sector = 1
    )

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports

class L1ICache(CompressedL1Cache):
    """L1 Instruction Cache with FPC compression."""
    
    # Optionally override specific parameters for I-cache if needed
    assoc = 8 # Often higher associativity for I-cache
    
    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port

class L1DCache(CompressedL1Cache):
    """L1 Data Cache with FPC compression."""
    
    # Often lower associativity for D-cache
    assoc = 2
    
    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port

# --- 2. Simulation Setup and Execution ---

# Setup argument parsing
SimpleOpts.add_option('--binary', default=None, help="The binary to execute.")
args = SimpleOpts.parse_args()

# Set default binary if none provided (e.g., gem5's simple hello world)
if not args.binary:
    thispath = os.path.dirname(os.path.realpath(__file__))
    args.binary = os.path.join(thispath, '../../', 'tests/test-progs/hello/bin/x86/linux/hello')

# 2.1 System and Clock Domain
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '2GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('256MiB')]

# 2.2 CPU and Caches
system.cpu = X86TimingSimpleCPU()
system.cpu.dcache = L1DCache()
system.cpu.icache = L1ICache()

# 2.3 Bus and Connections
system.membus = SystemXBar()

# Connect caches to CPU and Bus
system.cpu.dcache.connectCPU(system.cpu)
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectBus(system.membus)
system.cpu.icache.connectBus(system.membus)

# Interrupt Controller (Required for x86)
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

# 2.4 Memory Controller
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# 2.5 Workload Setup (SE Mode)
system.workload = SEWorkload.init_compatible(args.binary)
process = Process()
process.cmd = [args.binary]
system.cpu.workload = process
system.cpu.createThreads()

# 2.6 Instantiate and Run
root = Root(full_system=False, system=system)
m5.instantiate()

print(f'Starting simulation using compressed L1I/L1D caches with FPCD.')
exit_event = m5.simulate()

print(f'Exiting @ tick {m5.curTick()} because {exit_event.getCause()}')