import matplotlib.pyplot as plt

bm_throughputs = [130347889.7, 15166967, 132483392.3] #8 Nodes, 4 Cores per Node | 8 executors, 1 core

colors  = ['skyblue', 'lightgreen', 'lightcoral']
hatches = ['/', '\\', 'x']

benchmarks = ['Sort', 'Join', 'RF']

x = range(len(benchmarks))

bars = plt.bar(x, bm_throughputs, color=colors, hatch=hatches)

plt.xlabel('Benchmarks')
plt.ylabel('Throughput (B/s)')
plt.title('8 Nodes, 4 Cores per Node | 8 executors, 1 core')
plt.xticks(x, benchmarks)

plt.ylim(0, max(bm_throughputs) + 10000000)

legend_labels = ['Sort', 'Join', 'Random Forest']
plt.legend(bars, legend_labels)
plt.tight_layout()
plt.savefig('figures/' + 'workloads' + '_benchmark.png')
plt.show()