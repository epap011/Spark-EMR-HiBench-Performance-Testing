import matplotlib.pyplot as plt
import numpy as np

def autolabel(rects, data):
    for rect, val in zip(rects, data):
        height = rect.get_height()
        ax.annotate('{}'.format(val),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

sort_throughputs = [137340726, 176128006]
join_throughputs = [130904746, 182072990]
rf_throughputs   = [15200433 , 27370327]

sort_duration = ["237s", "184s"]
join_duration   = ["145s", "104s"]
rf_duration = ["1578s", "876s"]

BENCHMARK = "RF" # Sort, Join, RF

fig, ax = plt.subplots()

bar_width = 0.35

index = np.arange(3)

if BENCHMARK == 'Sort':
    rects1 = ax.bar(1 - bar_width/2, sort_throughputs[0], bar_width, label='Machine 1', color='skyblue', hatch='/')
    rects2 = ax.bar(1 + bar_width/2, sort_throughputs[1], bar_width, label='Machine 2', color='lightcoral', hatch='\\')
    autolabel(rects1, [sort_duration[0]])
    autolabel(rects2, [sort_duration[1]])

elif BENCHMARK == 'Join':
    rects3 = ax.bar(2 - bar_width/2, join_throughputs[0], bar_width, label='Machine 1', color='skyblue', hatch='/')
    rects4 = ax.bar(2 + bar_width/2, join_throughputs[1], bar_width, label='Machine 2', color='lightcoral', hatch='\\')
    autolabel(rects3, [join_duration[0]])
    autolabel(rects4, [join_duration[1]])

elif BENCHMARK == 'RF':
    rects5 = ax.bar(3 - bar_width/2, rf_throughputs[0], bar_width, label='Machine 1', color='skyblue', hatch='/')
    rects6 = ax.bar(3 + bar_width/2, rf_throughputs[1], bar_width, label='Machine 2', color='lightcoral', hatch='\\')
    autolabel(rects5, [rf_duration[0]])
    autolabel(rects6, [rf_duration[1]])

def autolabel(rects, data):
    for rect, val in zip(rects, data):
        height = rect.get_height()
        ax.annotate('{}'.format(val),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.set_xlabel(BENCHMARK + ' Benchmark')
ax.set_ylabel('Throughput (B/s)')
if BENCHMARK == 'Sort':
    ax.set_ylim(0, max(sort_throughputs) + 70000000)
elif BENCHMARK == 'Join':
    ax.set_ylim(0, max(join_throughputs) + 12000000)
elif BENCHMARK == 'RF':
    ax.set_ylim(0, max(rf_throughputs)   + 10000000)
ax.set_xticks([])
ax.legend(["8 x m5.xlarge", "4 x m5.2xlarge"])

plt.savefig('figures/' + 'experiment_4_' + BENCHMARK + '_results.png')
plt.show()