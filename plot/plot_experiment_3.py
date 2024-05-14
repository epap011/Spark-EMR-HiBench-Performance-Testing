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

BENCHMARK = 'Join'  # Sort, Join, RF

sort_throughputs = [137340726, 145664318, 144619121]
join_throughputs = [130904746, 130050001, 132004908]
rf_throughputs   = [15200433, 15248537, 14767638]

sort_duration = ["237s", "223s", "225s"]
join_duration = ["145s", "146s", "144s"]
rf_duration   = ["1578s", "1573s", "1625s"]

colors = ['skyblue', 'lightcoral', 'lightgreen']

fig, ax = plt.subplots()

bar_width = 0.20

if BENCHMARK == 'Sort':
    rects1 = ax.bar(1 - bar_width * 1.05, [sort_throughputs[0]], bar_width, label='8 Workers', color=colors[0], hatch='/')
    rects2 = ax.bar(1, [sort_throughputs[1]], bar_width, label='10 Workers', color=colors[1], hatch='\\')
    rects3 = ax.bar(1 + bar_width * 1.05, [sort_throughputs[2]], bar_width, label='12 Workers', color=colors[2], hatch='x')
    autolabel(rects1, [sort_duration[0]])
    autolabel(rects2, [sort_duration[1]])
    autolabel(rects3, [sort_duration[2]])

elif BENCHMARK == 'Join':
    rects4 = ax.bar(1 - bar_width * 1.05, [join_throughputs[0]], bar_width, label='8 Workers', color=colors[0], hatch='/')
    rects5 = ax.bar(1, [join_throughputs[1]], bar_width, label='10 Workers', color=colors[1], hatch='\\')
    rects6 = ax.bar(1 + bar_width * 1.05, [join_throughputs[2]], bar_width, label='12 Workers', color=colors[2], hatch='x')
    autolabel(rects4, [join_duration[0]])
    autolabel(rects5, [join_duration[1]])
    autolabel(rects6, [join_duration[2]])

elif BENCHMARK == 'RF':
    rects7 = ax.bar(1 - bar_width * 1.05, [rf_throughputs[0]], bar_width, label='8 Workers', color=colors[0], hatch='/')
    rects8 = ax.bar(1, [rf_throughputs[1]], bar_width, label='10 Workers', color=colors[1], hatch='\\')
    rects9 = ax.bar(1 + bar_width * 1.05, [rf_throughputs[2]], bar_width, label='12 Workers', color=colors[2], hatch='x')
    autolabel(rects7, [rf_duration[0]])
    autolabel(rects8, [rf_duration[1]])
    autolabel(rects9, [rf_duration[2]])

ax.set_xlabel(BENCHMARK + ' Benchmark')
ax.set_ylabel('Throughput (B/s)')

if BENCHMARK == 'Sort':
    ax.set_ylim(0, max(sort_throughputs) + 10000000)
elif BENCHMARK == 'Join':
    ax.set_ylim(0, max(join_throughputs) + 40000000)
elif BENCHMARK == 'RF':
    ax.set_ylim(0, max(rf_throughputs)   + 5000000)
ax.set_xticks([])
ax.legend()
plt.tight_layout()
plt.savefig('figures/' + 'experiment_3_' + BENCHMARK + '_results.png')
plt.show()
