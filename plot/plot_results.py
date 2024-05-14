import matplotlib.pyplot as plt

pairs = [(1, 8), (2, 4), (4, 2), (8, 1)]
x = range(len(pairs))

benchmark_name = 'RF' #Sort, Join, RF
sort_throughputs = [0, 66478945, 108372833, 137340726]
join_throughputs = [0, 51698833, 91748746, 130904746]
rf_throughputs   = [0, 4484625, 9659282, 15200433]

colors  = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon']
hatches = ['/', '\\', 'x', '-']

if benchmark_name == 'Sort':
    bars = plt.bar(x, sort_throughputs, color=colors, hatch=hatches)
elif benchmark_name == 'Join':
    bars = plt.bar(x, join_throughputs, color=colors, hatch=hatches)
elif benchmark_name == 'RF':
    bars = plt.bar(x, rf_throughputs, color=colors, hatch=hatches)

plt.xlabel('(Executors, Cores)')
plt.ylabel('Throughput (B/s)')
plt.title(benchmark_name + ' Benchmark: Gigantic Workload')
plt.xticks(x, [str(pair) for pair in pairs])

if benchmark_name == 'Sort':
    plt.ylim(0, max(sort_throughputs) + 10000000)
elif benchmark_name == 'Join':
    plt.ylim(0, max(join_throughputs) + 10000000)
elif benchmark_name == 'RF':
    plt.ylim(0, max(rf_throughputs) + 10000000)

legend_labels = ['1 Executors, 8 Cores', '2 Executors, 4 Cores', '4 Executors, 2 Cores', '8 Executors, 1 Cores']
plt.legend(bars, legend_labels)
plt.tight_layout()
plt.savefig('figures/' + benchmark_name + '_benchmark.png')
plt.show()