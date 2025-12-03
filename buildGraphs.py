import re
import pandas as pd
import matplotlib.pyplot as plt

# =====================
# CONFIG
stats_file = "stats.txt"  # Path to Gem5 stats file
cache_line_bits = 512     # Assume uncompressed cache line size in bits
# =====================

# 1. Read the stats file
with open(stats_file, 'r') as f:
    lines = f.readlines()

# 2. Parse the stats into a dictionary
stats = {}
for line in lines:
    # Match lines like: name value # comment
    match = re.match(r'(\S+)\s+([\d.eE+-]+)', line)
    if match:
        key, value = match.groups()
        stats[key] = float(value)

# 3. Extract cache compression metrics
compressions = stats.get("system.cpu.dcache.compressor.compressions", 0)
failed = stats.get("system.cpu.dcache.compressor.failedCompressions", 0)
decompressions = stats.get("system.cpu.dcache.compressor.decompressions", 0)
total_bits = stats.get("system.cpu.dcache.compressor.compressionSizeBits", 0)
avg_bits = stats.get("system.cpu.dcache.compressor.avgCompressionSizeBits", 0)

# Derived metrics
success_rate = compressions / (compressions + failed) if (compressions + failed) > 0 else 0
compression_ratio = cache_line_bits / avg_bits if avg_bits > 0 else 0

# 4. Extract simulation performance metrics
sim_seconds = stats.get("simSeconds", 0)
sim_insts = stats.get("simInsts", 0)
sim_cycles = stats.get("system.cpu.numCycles", 0)
ipc = stats.get("system.cpu.ipc", 0)
cpi = stats.get("system.cpu.cpi", 0)

# 5. Print summary
print("=== Cache Compression Metrics ===")
print(f"Total compressions: {compressions}")
print(f"Failed compressions: {failed}")
print(f"Compression success rate: {success_rate:.2f}")
print(f"Total compressed bits: {total_bits}")
print(f"Average compressed size per block: {avg_bits:.2f} bits")
print(f"Compression ratio (uncompressed/avg): {compression_ratio:.2f}")
print(f"Decompressions: {decompressions}")

print("\n=== Simulation Performance Metrics ===")
print(f"Simulated seconds: {sim_seconds}")
print(f"Instructions simulated: {sim_insts}")
print(f"CPU cycles simulated: {sim_cycles}")
print(f"IPC: {ipc}")
print(f"CPI: {cpi}")

# 6. Plot metrics
metrics = {
    "Compression success rate": success_rate,
    "Compression ratio": compression_ratio,
    "Average compressed size (bits)": avg_bits,
    "Decompressions (x1000)": decompressions / 1000,
    "IPC": ipc,
    "CPI": cpi
}

fig, ax = plt.subplots(figsize=(10,6))
names = list(metrics.keys())
values = list(metrics.values())
ax.barh(names, values, color='skyblue')
ax.set_xlabel("Value")
ax.set_title("Gem5 Cache Compression & Performance Metrics")
plt.tight_layout()
plt.show()