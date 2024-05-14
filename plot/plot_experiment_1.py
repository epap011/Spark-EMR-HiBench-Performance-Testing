import matplotlib.pyplot as plt

pairs = [(1, 8), (2, 4), (4, 2), (8, 1)]
x = range(len(pairs))

benchmark_name = 'Join' #Sort, Join, RF
sort_throughputs = [0, 66478945, 108372833, 137340726]
join_throughputs = [0, 51698833, 91748746, 130904746]
rf_throughputs   = [0, 4484625, 9659282, 15200433]

sort_duration = ["0s", "490s", "300s", "237s"]
join_duration = ["0s", "367s", "207s", "145s"]
rf_duration   = ["0s", "5351s", "2484s", "1578s"]

colors  = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon']
hatches = ['/', '\\', 'x', '-']

if benchmark_name == 'Sort':
    bars = plt.bar(x, sort_throughputs, color=colors, hatch=hatches)
elif benchmark_name == 'Join':
    bars = plt.bar(x, join_throughputs, color=colors, hatch=hatches)
elif benchmark_name == 'RF':
    bars = plt.bar(x, rf_throughputs, color=colors, hatch=hatches)


def autolabel(rects, data):
    for rect, val in zip(rects, data):
        height = rect.get_height()
        plt.annotate('{}'.format(val),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')

if benchmark_name == 'Sort':
    autolabel(bars, [sort_duration[0], sort_duration[1], sort_duration[2], sort_duration[3]])
elif benchmark_name == 'Join':
    autolabel(bars, [join_duration[0], join_duration[1], join_duration[2], join_duration[3]])
elif benchmark_name == 'RF':
    autolabel(bars, [rf_duration[0], rf_duration[1], rf_duration[2], rf_duration[3]])

plt.xlabel('(Executors, Cores)')
plt.ylabel('Throughput (B/s)')
plt.xticks(x, [str(pair) for pair in pairs])

if benchmark_name == 'Sort':
    plt.ylim(0, max(sort_throughputs) + 10000000)
elif benchmark_name == 'Join':
    plt.ylim(0, max(join_throughputs) + 10000000)
elif benchmark_name == 'RF':
    plt.ylim(0, max(rf_throughputs) + 1000000)

legend_labels = ['1 Executors, 8 Cores, 2GB', '2 Executors, 4 Cores, 4GB', '4 Executors, 2 Cores, 4GB', '8 Executors, 1 Cores, 2GB']
plt.legend(bars, legend_labels)
plt.tight_layout()
plt.savefig('figures/experiment_1_' + benchmark_name + '_results.png')
plt.show()