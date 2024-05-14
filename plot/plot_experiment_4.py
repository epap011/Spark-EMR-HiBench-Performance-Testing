import matplotlib.pyplot as plt
import numpy as np

sort_throughputs = [137340726, 176128006]
join_throughputs = [130904746, 182072990]
rf_throughputs   = [15200433 , 27370327]

sort_duration = ["237s", "184s"]
join_duration   = ["145s", "104s"]
rf_duration = ["1578s", "876s"]

fig, ax = plt.subplots()

bar_width = 0.35

index = np.arange(3)

rects1 = ax.bar(index[0] - bar_width/2, sort_throughputs[0], bar_width, label='Machine 1', color='skyblue', hatch='/')
rects2 = ax.bar(index[0] + bar_width/2, sort_throughputs[1], bar_width, label='Machine 2', color='lightcoral', hatch='\\')

rects3 = ax.bar(index[1] - bar_width/2, join_throughputs[0], bar_width, label='Machine 1', color='skyblue', hatch='/')
rects4 = ax.bar(index[1] + bar_width/2, join_throughputs[1], bar_width, label='Machine 2', color='lightcoral', hatch='\\')

rects5 = ax.bar(index[2] - bar_width/2, rf_throughputs[0], bar_width, label='Machine 1', color='skyblue', hatch='/')
rects6 = ax.bar(index[2] + bar_width/2, rf_throughputs[1], bar_width, label='Machine 2', color='lightcoral', hatch='\\')

def autolabel(rects, data):
    for rect, val in zip(rects, data):
        height = rect.get_height()
        ax.annotate('{}'.format(val),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1, [sort_duration[0]])
autolabel(rects2, [sort_duration[1]])
autolabel(rects3, [join_duration[0]])
autolabel(rects4, [join_duration[1]])
autolabel(rects5, [rf_duration[0]])
autolabel(rects6, [rf_duration[1]])

ax.set_xlabel('Benchmark')
ax.set_ylabel('Throughput (B/s)')
ax.set_ylim(0, max(sort_throughputs + join_throughputs + rf_throughputs) + 20000000)
ax.set_xticks(index)
ax.set_xticklabels(['Sort', 'Join', 'Random Forest'])
ax.legend(["8 x m5.xlarge", "4 x m5.2xlarge"])

plt.savefig('figures/' + 'experiment_4' + '_results.png')
plt.show()
